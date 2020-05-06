import logging
from furl import furl

from ..utils import my_util_functions as my_utils

logger = logging.getLogger(__name__)
db_drivers = my_utils.load_drivers(drivers_path="./brainstreamer/databases/db_drivers", driver_type="class")


class DBWrapper:
    def __init__(self, url):
        url = furl(url)
        scheme, host, port = url.scheme, url.host, url.port

        if scheme not in db_drivers:
            raise ValueError(f"Unsupported DB driver: {scheme}")
        self.db = db_drivers[scheme](host, port)
        self.logger = logger

    def __repr__(self):
        return self.db.__repr__()

    def insert_user(self, user):
        self.db.insert_user(user)

    def insert_results(self, data):
        self.db.insert_results(data)

    def get_users(self):
        return self.db.get_users()

    def get_user_by_id(self, user_id):
        return self.db.get_user_by_id(user_id)

    def get_snapshots_by_user_id(self, user_id):
        return self.db.get_snapshots_by_user_id(user_id)

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return self.db.get_snapshot_by_id(user_id, snapshot_id)
