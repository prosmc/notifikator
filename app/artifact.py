 # -*- coding: utf-8 -*-

from flask import current_app
from elasticsearch import client
from .utils import IndexName
import requests
from requests.auth import HTTPBasicAuth
import json

class Artifact:

    def __init__(self, app):
        self.app = app
        
    def set_client(self, es_client, url_client):
        (self.es_client, self.url_client) = (es_client, url_client)

    def is_alias(self, es_client, name):
        resp = None
        with self.app.app_context():
            try:
                indices_client = client.IndicesClient(es_client)
                resp = indices_client.exists_alias(name=name)
                current_app.logger.debug(f"Alias '{name}' exists: {resp}")
                current_app.logger.info(f"Elasticsearch alias lookup was successfully.")
            except Exception as other:
                current_app.logger.error(f"Elasticsearch alias lookup exception occured: {other}")
        return resp

    def create_index_ilm_policy(self, es_client, name, data):
        with self.app.app_context():
            try:
                ilm_client = client.ilm.IlmClient(es_client)
                ilm_client.put_lifecycle(policy=name, body=data)
                current_app.logger.info(f"Elasticsearch ILM policy '{ name }' was successfully created.")
            except Exception as other:
                current_app.logger.error(f"Elasticsearch ILM policy creation exception occured: {other}")

    def exists_index_ilm_policy(self, es_client, name):
        with self.app.app_context():
            try:
                ilm_client = client.ilm.IlmClient(es_client)
                res = ilm_client.get_lifecycle(policy=name)
                current_app.logger.info(res)
                if res is not None:
                    current_app.logger.info(f"Elasticsearch ILM policy '{ name }' does exist.")
                else:
                    current_app.logger.info(f"Elasticsearch ILM policy '{ name }' does not exist.")
            except Exception as other:
                current_app.logger.info(f"Elasticsearch ILM policy '{ name }' can't be checked for existence.")
                
    def create_index_template(self, es_client, name, data):
        with self.app.app_context():
            try:
                indices_client = client.IndicesClient(es_client)
                indices_client.put_template(name=name, body=data)
                current_app.logger.info(f"Elasticsearch index template '{ name }' was successfully created.")
            except Exception as other:
               current_app.logger.error(f"Elasticsearch index template creation exception occured: {other}")

    def create_index(self, es_client, name, data):
        with self.app.app_context():
            try:
                if not self.is_alias(es_client, name):
                    indices_client = client.IndicesClient(es_client)
                    indices_client.create(index=IndexName.format(name), body=data)
                    current_app.logger.info(f"Elasticsearch index '{ name }' was successfully created.")
            except Exception as other:
                current_app.logger.error(f"Elasticsearch index creation exception occured: {other}")

    def create_index_pattern(self, client, **kwargs):
        with self.app.app_context():
            try:
                headers = {
                    'kbn-xsrf': 'true'
                }
                resp = client.perform_request(
                    method='POST',
                    url=kwargs.get('url'), 
                    auth=HTTPBasicAuth(self.app.config['APP_KB_USER'], self.app.config['APP_KB_PASSWORD']), 
                    data=kwargs.get('data'),
                    headers=headers,
                    verify=eval(self.app.config['APP_KB_VERIFY_CERTS'])
                )
                current_app.logger.info(resp)
                current_app.logger.info(f"Kibana Korrelator index_pattern '{kwargs.get('name')}' successfully created.")
            except Exception as other:
                current_app.logger.error(f"Kibana Korrelator index_pattern '{kwargs.get('name')}' creation exception occured: {other}")

    def create_search_template(self, url_client, http_method, name, data ):
        with self.app.app_context():
            try:
                url = "/_scripts/" + name
                url_client.perform_request(http_method, url, body=data)
                current_app.logger.info(f"Elasticsearch search template '{ url }' was successfully created.")
            except Exception as other:
                current_app.logger.error(f"Elasticsearch search template '{ url }' exception occured: {other}")

    def create_watch(self, es_client, watch_id, watch_data):
        with self.app.app_context():
            try:
                watcher_client = client.watcher.WatcherClient(es_client)
                watcher_client.put_watch(id=watch_id, body=watch_data)
                current_app.logger.info(f"Elasticsearch watch '{ watch_id }' was successfully created.")
            except Exception as other:
                current_app.logger.error(f"Elasticsearch watch '{ watch_id }' exception occured: {other}")
                
    def create_dashboard(self, client, data):
        with self.app.app_context():
            try:
                REQUEST_URL=f"https://{self.app.config['APP_KB_HOST']}:{self.app.config['APP_KB_PORT']}/api/saved_objects/_import"
                headers = {
                    'kbn-xsrf': 'true'
                }
                files = {'file': ('request.ndjson', data) }
                resp = client.perform_request(
                    method='POST',
                    url=REQUEST_URL, 
                    auth=HTTPBasicAuth(self.app.config['APP_KB_USER'], self.app.config['APP_KB_PASSWORD']), 
                    files=files, 
                    headers=headers,
                    verify=eval(self.app.config['APP_KB_VERIFY_CERTS'])
                )
                current_app.logger.info(resp)
                current_app.logger.info(f"Kibana Korrelator dashboard was successfully created.")
            except Exception as other:
                current_app.logger.error(f"Kibana Korrelator dashboard creation exception occured: {other}")