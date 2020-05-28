import requests
from brainstreamer.platforms import ReaderWrapper
from brainstreamer.platforms.protocols.protocol_drivers import client_server_protobuf
import logging
from tqdm import tqdm


def upload_sample(host, port, num_of_snaps_to_read, sample_path):
    logger = logging.getLogger(__name__)
    logger.debug(f"{host}, {port}")
    logger.debug("running client")

    reader = ReaderWrapper(sample_path)
    logger.debug("initialized reader")

    user = reader.get_user()
    logger.debug("read user successfully")

    snapshots_uploaded = 0
    snapshots_iter = tqdm(reader, total=num_of_snaps_to_read,
                          desc="Uploading samples: ") if num_of_snaps_to_read \
        else tqdm(reader, desc="Uploading samples: ")

    try:
        for snapshot in snapshots_iter:
            if num_of_snaps_to_read and snapshots_uploaded == num_of_snaps_to_read:
                break
            snapshots_uploaded += 1

            url = f'http://{host}:{port}/snapshot'
            logger.debug(f"posting snapshot to server on url: {url} ")
            r = requests.post(url=url, data=client_server_protobuf.serialize_message(user, snapshot))

            if r.status_code == 200:
                logger.debug(f"client posted snapshot number {snapshots_uploaded} successfully")
            else:
                logger.error(f"client failed to post snapshot number {snapshots_uploaded} to server")


    except KeyboardInterrupt:
        print(f'Brain streaming stopped. total number of {snapshots_uploaded} snapshots were uploaded')
        return

    print(f"Brain Streaming succeeded. All the {snapshots_uploaded} snapshots were uploaded!")
    logger.debug(f"Brain Streaming succeeded. All the {snapshots_uploaded} snapshots were uploaded!")
