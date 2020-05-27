import json
import logging

from brainstreamer.platforms.message_queue import MqWrapper
from brainstreamer.platforms.protocols import client_server_protocol, server_mq_protocol, process_protocol_data

from flask import Flask, request
from brainstreamer.utils import FileSystemHandler as FSH

app = Flask(__name__)
logger = logging.getLogger(__name__)
url = None


def run(host, port, mq_url):
    logger.debug("running server")

    global url
    url = mq_url
    app.run(host=host, port=port)


@app.route('/snapshot', methods=['POST'])
def post_snapshot():
    # Get and build the user, snapshot proto-buf objects
    user, snapshot = client_server_protocol.deserialize_message(request.get_data())
    logger.debug(f"server got snapshot from user: {user.username}")

    # Process the user and snapshot objects to custom made dicts, suitable for the json protocol
    user_dict, snapshot_dict = process_protocol_data(user, snapshot)

    # Prepare image data for saving
    color_image_data = snapshot.color_image.data
    depth_image_data = json.dumps(list(snapshot.depth_image.data))

    logger.debug(f"saving images")
    # Save image data in file system (using the file system manager)
    FSH.save(snapshot_dict['color_image_path'], color_image_data)
    FSH.save(snapshot_dict['depth_image_path'], depth_image_data)

    # Encode the user, snapshot using json protocol
    json_user = server_mq_protocol.encode(user_dict)
    json_snapshot = server_mq_protocol.encode(snapshot_dict)

    try:
        mq = MqWrapper(url)
        mq.publish('user', json_user)
        mq.publish('snapshot', json_snapshot)
    except ConnectionError:
        raise ConnectionError("Server failure: received a message from client,"
                              " but couldn't connect to queue")

    return ""
