from .readers.reader import Reader
from . import cognition_protocol as cp
import logging
import requests


def run(address, sample_path):
    logger = logging.getLogger(__name__)
    logger.debug(f"{address}")
    logger.debug("running client")

    reader = Reader(sample_path + "/sample.mind.gz")
    logger.debug("initialized reader")

    user = reader.get_user()
    logger.debug("read user successfully")

    snapshot = reader.get_snapshot()
    logger.debug("read snapshot successfully")

    host, port = address
    url = f'http://{host}:{port}/snapshot'

    logger.debug(f"posting snapshot to server on url: {url} ")
    r = requests.post(url=url, data=cp.serialize_message(user, snapshot))

    if r.status_code == 200:
        logging.debug("client posted snapshot successfully")
    else:
        logging.error("client failed to post snapshot to server")
