 # -*- coding: utf-8 -*-
 
import os
import sys
import logging
import threading
import atexit

from flask import Flask, current_app
from .config import config
from logging.config import dictConfig
from .logger import Logger
from .bootstrap import Bootstrap

def create_app(*args, **kwargs):
    """Create and configure an instance of the Flask application."""
    env = kwargs.get('env', 'live')
    config_name = kwargs.get('config_name', 'testing')
    app = Flask(__name__, instance_relative_config=True)

    # CONFIGURATION DEFINITIONS
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['APP_ILM_POLICY_TEMPLATES'] = { 
        app.config['APP_ES_INDEX_02']: 'policy_01.json.j2'
    }
    app.config['APP_INDEX_TEMPLATES'] = { 
        app.config['APP_ES_INDEX_02']: 'template_01.json.j2'
    }
    app.config['APP_INDICES'] = { 
        app.config['APP_ES_INDEX_02']: 'index_01.json.j2'
    }
    app.config['APP_INDEX_QUERIES'] = { 
        'query-01': {
            'template_path': 'templates/elasticsearch',
            'script_template_file': 'script-01.json.j2',
            'query_template_file' : 'query-01.json.j2'
        },
        'query-02': {
            'template_path': 'templates/elasticsearch',
            'script_template_file': 'script-02.json.j2',
            'query_template_file' : 'query-02.json.j2'
        },
        'query-03': {
            'template_path': 'templates/elasticsearch',
            'script_template_file': 'script-03.json.j2',
            'query_template_file' : 'query-03.json.j2'
        }
    }

    # ENSURE THE INSTANCE FOLDER EXISTS!
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    bootstrap = Bootstrap(app)
    bootstrap.startup()

    return app