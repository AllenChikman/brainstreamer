import logging
from . import cognition_protocol as cp
from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger(__name__)

def run(address):
    host, port = address

    logger.debug("running server")
    app.run(host=host, port=port)


@app.route('/snapshot', methods=['POST'])
def post_snapshot():
    message_bytes = request.get_data()
    user, snapshot = cp.deserialize_message(message_bytes)
    logger.debug(f"server got snapshot from user: {user.username}")





    return ""



