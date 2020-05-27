import json

data_dir = './brainstreamer/data/protocol_shared_data'


def get_data_path():
    return data_dir


def encode(arranged_dict):
    return json.dumps(arranged_dict, indent=4)


def decode(target_dict):
    return json.loads(target_dict)

