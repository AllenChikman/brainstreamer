'''
This module's role  is to manage the whole communication with the file system
'''

import logging
import os
import os.path
import errno

logger = logging.getLogger(__name__)


def _mkdir_p(path):
    logger.debug(f"creating file: {path}")
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def _safe_open(path, mode):
    # Open "path" for writing, creating any parent directories as needed.

    _mkdir_p(os.path.dirname(path))
    return open(path, mode)


class FileSystemHandler:
    @staticmethod
    def save(path, data):
        mode = 'wb+' if type(data) == bytes else 'w+'
        with _safe_open(path, mode) as f:
            f.write(data)

    @staticmethod
    def load(path, byte=False):
        mode = 'rb' if byte else 'r'
        with _safe_open(path, mode) as f:
            return f.read()

    # create the father directories of the desired directory, if not exists
    @staticmethod
    def safe_create_dir(dir_path):
        _mkdir_p(dir_path)
