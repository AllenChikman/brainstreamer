import requests

from brainstreamer.platforms.protocols.cogintion_pb_protocol.reader import Reader
from brainstreamer.platforms.protocols.cogintion_pb_protocol import cognition_pb_protocol as cp
import logging
from tqdm import tqdm


def run(host, port, num_of_snaps_to_read, sample_path):
    logger = logging.getLogger(__name__)
    logger.debug(f"{host}, {port}")
    logger.debug("running client")

    reader = Reader(sample_path)
    logger.debug("initialized reader")

    user = reader.get_user()
    logger.debug("read user successfully")

    snapshots_uploaded = 0

    pbar = tqdm(total=num_of_snaps_to_read) if num_of_snaps_to_read else None

    try:
        for snapshot in reader:
            if pbar:
                pbar.update(1)
                pbar.set_description("Uploading samples: ")
            logger.debug("read snapshot successfully")
            url = f'http://{host}:{port}/snapshot'

            logger.debug(f"posting snapshot to server on url: {url} ")
            r = requests.post(url=url, data=cp.serialize_message(user, snapshot))

            if r.status_code == 200:
                logger.debug("client posted snapshot successfully")
            else:
                logger.error("client failed to post snapshot to server")

            snapshots_uploaded += 1
            if num_of_snaps_to_read and snapshots_uploaded == num_of_snaps_to_read:
                break
    except KeyboardInterrupt:
        print(f'Brain streaming stopped. total number of {snapshots_uploaded} snapshots were uploaded')
        return

    print(f"Brain Streaming succeeded. All the {snapshots_uploaded} snapshots were uploaded!")
    logger.debug(f"Brain Streaming succeeded. All the {snapshots_uploaded} snapshots were uploaded!")
