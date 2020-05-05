import datetime as dt
import uuid
import logging


def init_logger(logger_file_name):
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename=f'./brainstreamer/debug_logs/{logger_file_name}_log.txt', level=logging.DEBUG, format=log_format,
                        datefmt='%m/%d/%Y %H:%M:%S', filemode='w')
    logging.getLogger("pika").setLevel(logging.WARNING)
    logging.getLogger("werkzeug").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def epoch_to_date(seconds, date_format="%d/%m/%Y, %H:%M:%S:%f"):
    datetime = dt.datetime.fromtimestamp(seconds).strftime(date_format)
    return datetime


def get_unique_id():
    return str(uuid.uuid4())
