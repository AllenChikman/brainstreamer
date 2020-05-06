import datetime as dt
import uuid
import logging
import sys
import importlib
from pathlib import Path


def init_logger(logger_file_name):
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename=f'./brainstreamer/data/debug_logs/{logger_file_name}_log.txt', level=logging.DEBUG,
                        format=log_format,
                        datefmt='%m/%d/%Y %H:%M:%S', filemode='w')
    logging.getLogger("pika").setLevel(logging.WARNING)
    logging.getLogger("werkzeug").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def epoch_to_date(seconds, date_format="%d/%m/%Y, %H:%M:%S:%f"):
    datetime = dt.datetime.fromtimestamp(seconds).strftime(date_format)
    return datetime


def get_unique_id():
    return str(uuid.uuid4())


def load_drivers(drivers_path, driver_type):
    loaded_modules = set()
    drivers = {}

    # Add absolute path to sys for module importing
    root = Path(drivers_path).absolute()
    sys.path.insert(0, str(root.parent))

    # go through every file in the drivers' dir and check if it good for importing as a module
    for file in root.iterdir():
        if file.suffix == '.py' and not file.name.startswith('_'):
            module = importlib.import_module(f'{root.name}.{file.stem}', package=root.name)
            loaded_modules.add(module)

    # for ever class/function in the module, search for drivers with "scheme" attr and add them to the drivers dict
    for module in loaded_modules:
        if driver_type == "class":
            for key, cls in module.__dict__.items():
                if isinstance(cls, type) and hasattr(cls, "scheme"):
                    drivers[cls.scheme] = cls

        elif driver_type == "function":
            for key, func in module.__dict__.items():
                if callable(func) and hasattr(func, "scheme"):
                    drivers[func.scheme] = func

        else:
            raise ValueError(f"Unsupported driver type: {driver_type}")

    return drivers
