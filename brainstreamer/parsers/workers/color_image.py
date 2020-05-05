import json
from PIL import Image as PIL
from brainstreamer.utils import FileSystemHandler as FSHandler


def _prepare_img(width, height, path):
    size = width, height
    data = FSHandler.load(path, byte=True)
    image = PIL.frombytes('RGB', size, data)
    return image


def parse_color_image(snapshot):
    snapshot = json.loads(snapshot)

    user_id = snapshot["user_id"]
    snapshot_id = snapshot["snapshot_id"]

    width = snapshot["color_image_width"]
    height = snapshot["color_image_height"]
    path = snapshot["color_image_path"]

    image = _prepare_img(width, height, path)

    img_dir = f"./brainstreamer/public/snapshots_imgs/{user_id}/{snapshot_id}"
    FSHandler.safe_create_dir(img_dir)
    img_path = f"{img_dir}/color_img.png"
    image.save(img_path, 'PNG')
    return dict(data_path=img_path, image_width=width, image_height=height)


parse_color_image.topic = 'color_image'
