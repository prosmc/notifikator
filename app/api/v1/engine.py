from flask import jsonify, current_app, request
from app.api import bp
from app.engine import Engine
from app.processor import Processor
from app.utils import TimeStamp
import time


app_id = None
app_name = None
is_alive  = None

@bp.route('/engine', methods=['GET','POST'])
def start():
    global app_id, app_name, is_alive
    app_id = current_app.config['APP_ID']
    app_name = current_app.config['APP_NAME']
    thread = Engine.get_thread_by_name(app_id)
    if thread:
        is_alive = thread.is_alive()
    if request.method == 'POST':
        if not thread:
            processor = Processor(id=app_id, name=app_name, config=current_app.config, app=current_app._get_current_object())
            thread = Engine(target=Engine, name=app_id, processor=processor, interval=1)
            thread.start ()
            app_id = thread.getName()
            is_alive = thread.is_alive()
            Cache.startup_time = TimeStamp.format()
    return jsonify({"app_id": app_id, "is_alive": is_alive})


@bp.route('/engine/<string:id>', methods=['DELETE'])
def stop(id):
    global is_alive
    thread = Engine.get_thread_by_name(app_id)
    if thread:
        thread.stop()
        is_alive = False
    return jsonify({"app_id": app_id, "is_alive": is_alive})