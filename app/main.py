 # -*- coding: utf-8 -*-

from app import create_app
import logging
from .api import bp as api_bp
import os

config_name = os.environ.get("APP_CONFIG_NAME", "testing")
app = create_app(config_name=config_name)
app.register_blueprint(api_bp, url_prefix="/api/v1")

if __name__ == '__main__':
    app.run(debug=False, host=app.config['APP_IPADDRESS'],port=app.config['APP_PORT'])

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
