"""
This module manages the read of the sample file.
"""

import logging
from brainstreamer.utils import my_util_functions as my_utils

reader_drivers = my_utils.load_drivers(drivers_path="./brainstreamer/platforms/reader/reader_drivers",
                                       driver_type="class")


# This is a general Reader Wrapper
class ReaderWrapper:
    def __init__(self, path, file_reader_scheme="protobuf"):
        self.path = path
        self.file_reader = reader_drivers[file_reader_scheme](path)

        self.logger = logging.getLogger(__name__)
        self.logger.debug("Reader initialized")

    def get_user(self):
        self.logger.debug("getting user")
        return self.file_reader.get_user()

    def get_snapshot(self):
        self.logger.debug("getting snapshot")
        return self.file_reader.get_snapshot()

    def close(self):
        self.file_reader.stream.close()

    def __iter__(self):
        while snapshot := self.file_reader.get_snapshot():
            yield snapshot
