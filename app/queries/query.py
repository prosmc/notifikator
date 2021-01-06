# -*- coding: utf-8 -*-

from app.template import TemplateHandler
class QueryHandler:

    def __init__(self, app):
        self.app = app

    def get_search_query_result(self, **kwargs):
        with self.app.app_context():
            app_id           = self.app.config['APP_ID']
            client           = kwargs.get('client', None)
            index_name       = kwargs.get('index_name', None)
            template_path    = kwargs.get('template_path', None)
            template_file    = kwargs.get('template_file', None)
            template_handler = TemplateHandler(template_path=template_path)
            template_id      = kwargs.get('template_id', None)
            incident_id      = kwargs.get('incident_id', None)
            state            = kwargs.get('state', None)

            response = client.search_template(index=index_name, 
                                              body=template_handler.get_data(template_file, 
                                                    template_id=template_id, 
                                                    incident_id=incident_id, 
                                                    state=state))
            return response