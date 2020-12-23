from flask import jsonify, current_app
from app.api import bp


@bp.route('/', methods=['GET'])
def get_index():
    return jsonify(
                { 
                    "notifikator": { 
                        "name": current_app.config['APP_NAME'],
                        "id": current_app.config['APP_ID'],
                        "release": current_app.config['APP_RELEASE'], 
                        "config":   current_app.config['APP_CONFIG_NAME'],
                        "started": current_app.config['APP_STARTUP_TIME']
                    }                        
                }
            )