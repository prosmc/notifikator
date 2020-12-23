import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    APP_NAME = os.environ.get("APP_NAME", "Notifikator")
    APP_ID = os.environ.get("APP_ID", None)
    APP_CONFIG_NAME = os.environ.get("APP_CONFIG_NAME", "testing")
    APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION","Notifikator is an event notification service for Elasticsearch.")
    APP_RELEASE = os.environ.get("APP_RELEASE", None)
    APP_IPADDRESS = os.environ.get("APP_IPADDRESS", "127.0.0.1")
    APP_PORT = os.environ.get("APP_PORT", "5005")
    APP_THREAD_NUMB = os.environ.get("APP_THREAD_NUMB", 1)
    APP_SLEEP_TIME = os.environ.get("APP_SLEEP_TIME", 1)
    APP_FLASK_LOGGER = os.environ.get("APP_FLASK_LOGGER", True)
    APP_ES_SETUP_ARTIFACTS = os.environ.get("APP_ES_SETUP_ARTIFACTS", True)
    APP_KB_SETUP_ARTIFACTS = os.environ.get("APP_KB_SETUP_ARTIFACTS", True)
    APP_ES_BOOTSTRAP_RETRY_INTERVAL = os.environ.get("APP_ES_BOOTSTRAP_RETRY_INTERVAL", 1)
    APP_ES_BOOTSTRAP_RETRY_MAX = os.environ.get("APP_ES_BOOTSTRAP_RETRY_MAX", 300)
    APP_KB_BOOTSTRAP_RETRY_INTERVAL = os.environ.get("APP_KB_BOOTSTRAP_RETRY_INTERVAL", 1)
    APP_KB_BOOTSTRAP_RETRY_MAX = os.environ.get("APP_KB_BOOTSTRAP_RETRY_MAX", 300)
    APP_LOG_DIR = os.environ.get("APP_LOG_DIR", "./")
    APP_LOG_TYPE=os.environ.get("APP_LOG_TYPE", "stream")
    APP_LOG_LEVEL=os.environ.get("APP_LOG_LEVEL", "INFO")
    APP_MAIN_LOG_NAME = os.environ.get("APP_MAIN_LOG_NAME", "app.log")
    APP_WWW_LOG_NAME = os.environ.get("APP_WWW_LOG_NAME", "www.log")
    APP_LOG_MAX_BYTES = os.environ.get("APP_LOG_MAX_BYTES", 100_000_000) # 100MB in bytes
    APP_LOG_COPIES = os.environ.get("APP_LOG_COPIES", 5)
    APP_ES_HOST = os.environ.get("APP_ES_HOST", None)
    APP_ES_PORT = os.environ.get("APP_ES_PORT", None)
    APP_ES_USER = os.environ.get("APP_ES_USER", None)
    APP_ES_PASSWORD = os.environ.get("APP_ES_PASSWORD", None)
    APP_ES_INDEX_01 = os.environ.get("APP_ES_INDEX_01", "incident")
    APP_ES_INDEX_02 = os.environ.get("APP_ES_INDEX_02", "imticket")
    APP_ES_USE_SSL = os.environ.get("APP_ES_USE_SSL", "False")
    APP_ES_VERIFY_CERTS = os.environ.get("APP_ES_VERIFY_CERTS", False)
    APP_ES_CA_CERTS = os.environ.get("APP_ES_CA_CERTS", "/notifikator/resources/ssl/elasticsearch.cer")
    APP_ES_TEMPLATE_FOLDER = os.environ.get("APP_ES_TEMPLATE_FOLDER", "/notifikator/app/templates")
    APP_KB_HOST = os.environ.get("APP_KB_HOST", None)
    APP_KB_PORT = os.environ.get("APP_KB_PORT", None)
    APP_KB_VERIFY_CERTS = os.environ.get("APP_KB_VERIFY_CERTS", False)
    APP_KB_USER = os.environ.get("APP_KB_USER", None)
    APP_KB_PASSWORD = os.environ.get("APP_KB_PASSWORD", None)
    APP_KB_CA_CERTS = os.environ.get("APP_KB_CA_CERTS", "/notifikator/resources/ssl/kibana.cer")
    APP_KB_TEMPLATE_FOLDER = os.environ.get("APP_KB_TEMPLATE_FOLDER", "/notifikator/app/templates")

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
