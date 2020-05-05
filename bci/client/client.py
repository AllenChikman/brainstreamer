import requests

from bci.protocols.cogintion_pb_protocol.reader import Reader
from bci.protocols.cogintion_pb_protocol import cognition_pb_protocol as cp
import logging


def run(address, sample_path):
    logger = logging.getLogger(__name__)
    logger.debug(f"{address}")
    logger.debug("running client")

    reader = Reader(sample_path + "/sample.mind.gz")
    logger.debug("initialized reader")

    num_of_snapshots_to_read = 5

    user = reader.get_user()
    logger.debug("read user successfully")
    for i in range(num_of_snapshots_to_read):
        snapshot = reader.get_snapshot()
        logger.debug("read snapshot successfully")
        host, port = address
        url = f'http://{host}:{port}/snapshot'

        logger.debug(f"posting snapshot to server on url: {url} ")
        r = requests.post(url=url, data=cp.serialize_message(user, snapshot))

        if r.status_code == 200:
            logger.debug("client posted snapshot successfully")
        else:
            logger.error("client failed to post snapshot to server")
