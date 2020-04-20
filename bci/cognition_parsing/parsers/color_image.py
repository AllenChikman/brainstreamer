import json
from PIL import Image as PIL
from bci.utils import FileSystemHandler as FSH


def parse_color_image(snapshot):
    snapshot = json.loads(snapshot)
    width = snapshot["color_image_width"]
    height = snapshot["color_image_height"]
    path = snapshot["color_image_path"]

    size = width, height
    data = FSH.load(path, byte=True)
    image = PIL.frombytes('RGB', size, data)
    image.save("/home/user/brain-computer-interface/bci/protocols/shared_data/42/pic", 'PNG')
    return json.dumps({'data_path': path, 'image_width': width, 'image_height': height})


parse_color_image.field = 'color_image'
