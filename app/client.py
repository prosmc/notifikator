 # -*- coding: utf-8 -*-

from enum import Enum
from elasticsearch import Elasticsearch, Urllib3HttpConnection
from flask import current_app
from requests.auth import HTTPBasicAuth
import requests
import json

class ClientType(Enum):
    ELASTICSEARCH = 'Elasticsearch'
    KIBANA = 'Kibana'
    URLLIB3HTTPCONNECTION = 'Urllib3HttpConnection'

class Kibana():

    def __init__(self, app):
        self.app = app

    #def perform_request(self, method, url, auth, files, headers, verify, **kwargs):
    #    resp = requests.request(
    #                method=method,
    #                url=url,
    #                auth=auth,
    #                files=files,
    #                headers=headers,
    #                verify=verify,
    #                **kwargs
    #            )
    #    return resp

    def perform_request(self, **kwargs):
        resp = requests.request(**kwargs)
        return resp
          
class ClientFactory:

    @staticmethod
    def newInstance(type: ClientType, app):
        client = None
        es_use_ssl = True if app.config['APP_ES_USE_SSL'].lower() == "true" else False
        es_verify_certs = True if app.config['APP_ES_VERIFY_CERTS'].lower() == "true" else False

        if type.value == ClientType.ELASTICSEARCH.value:
            with app.app_context():
                try:
                    client = Elasticsearch([{'host': app.config['APP_ES_HOST'] ,'port': app.config['APP_ES_PORT'] }],
                                    http_auth=( app.config['APP_ES_USER'], app.config['APP_ES_PASSWORD']),
                                    use_ssl=es_use_ssl,
                                    verify_certs=es_verify_certs,
                                    ssl_show_warn=False,
                                    ca_certs=app.config['APP_ES_CA_CERTS'])
                except Exception as other:
                    current_app.logger.error(f"Can't establish {ClientType.ELASTICSEARCH.value} client connection {other}")
                finally:
                    return client      

        if type.value == ClientType.KIBANA.value:
            client = None
            with app.app_context():
                try:
                    client = Kibana(app)
                    REQUEST_URL=f"https://{app.config['APP_KB_HOST']}:{app.config['APP_KB_PORT']}/api/status"
                    client.perform_request(
                        method='GET',
                        url=REQUEST_URL, 
                        auth=HTTPBasicAuth(app.config['APP_KB_USER'], app.config['APP_KB_PASSWORD']),
                        files=None, 
                        headers=None,
                        verify=eval(app.config['APP_KB_VERIFY_CERTS'])
                    )
                except Exception as other:
                    current_app.logger.error(f"Can't establish {ClientType.KIBANA.value} client connection {other}")
                finally:
                    return client

        if type.value == ClientType.URLLIB3HTTPCONNECTION.value:
            with app.app_context():
                try:
                    client = Urllib3HttpConnection(host=app.config['APP_ES_HOST'],
                                    port=app.config['APP_ES_PORT'],
                                    http_auth=( app.config['APP_ES_USER'], app.config['APP_ES_PASSWORD']),
                                    use_ssl=es_use_ssl,
                                    verify_certs=es_verify_certs,
                                    ssl_show_warn=False,
                                    ca_certs=app.config['APP_ES_CA_CERTS'])
                except Exception as other:
                    current_app.logger.error(f"Can't establish {ClientType.URLLIB3HTTPCONNECTION.value} client connection {other}")
                finally:
                    return client

