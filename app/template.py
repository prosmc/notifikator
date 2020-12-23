 # -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from pathlib import Path
from flask import current_app
import json
import os

class TemplateHandler():

    def __init__(self, **kwargs):
        self.app = kwargs.get('app')
        template_path = kwargs.get('template_path')
        if template_path is not None:
            template_dir = os.path.join(os.path.dirname(__file__), template_path)
            self.env = Environment(
                autoescape=select_autoescape(['json']),
                loader=FileSystemLoader(template_dir),
                trim_blocks=True, 
                lstrip_blocks=True
            )
    
    def get_data(self, template, **kwargs):
        self.template = self.env.get_template(template)
        return json.dumps(json.loads(self.template.render(kwargs)))

    def get_raw_data(self, template, **kwargs):
        with self.app.app_context():
            data = None
            try:
                with open(template) as template_file:
                    data = template_file.read()
                return data
            except Exception as other:
                current_app.logger.error(f"Can't read file {template} - {other}")

    