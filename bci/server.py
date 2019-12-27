import os
import threading
import time
import struct
import click
from .utils.listener import Listener


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def append_to_file(path, text):
    f = open(path, "a")
    f.write(text)
    f.close()


class Handler(threading.Thread):
    lock = threading.Lock()

    def __init__(self, client, data_dir):
        super().__init__()
        self.client = client
        self.data_dir = data_dir

    def run(self):  # start invokes run

        chunk = self.client.receive(20)
        res = struct.unpack('QQi', chunk)

        thought_len = int(res[2])
        str_pack_format = str(thought_len) + 's'

        chunk = self.client.receive(thought_len)
        thought = struct.unpack(str_pack_format, chunk)

        formatted_date = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(res[1]))
        thought_str = thought[0].decode()

        dir_path = str(self.data_dir) + "/" + str(res[0])
        file_path = dir_path + "/" + formatted_date + ".txt"
        self.lock.acquire()
        create_dir(dir_path)
        if os.path.isfile(file_path):
            append_to_file(file_path, "\n")
        append_to_file(file_path, thought_str)
        self.lock.release()


def run_server(address, data):
    host, port = address
    listener = Listener(port, host)
    with listener:
        while True:
            client = listener.accept()
            handler = Handler(client, data)
            handler.start()


