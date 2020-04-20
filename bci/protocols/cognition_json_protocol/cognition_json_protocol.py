import json

data_dir = '/home/user/brain-computer-interface/bci/protocols/shared_data'


def get_data_path():
    return data_dir


def encode(arranged_dict):
    return json.dumps(arranged_dict, indent=4)


def decode(target_dict):
    return json.loads(target_dict)

