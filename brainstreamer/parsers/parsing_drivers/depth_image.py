import json
import numpy
import matplotlib
import matplotlib.pyplot as plt
from brainstreamer.utils import FileSystemHandler as FSHandler
import logging

logger = logging.getLogger(__name__)
BASE_IMG_DIR = "./brainstreamer/public/snapshots_imgs"


def _prepare_fig(width, height, path):
    size = height, width
    data = FSHandler.load(path, byte=True)
    data = json.loads(data)

    shaped = numpy.reshape(data, size)
    fig = plt.imshow(shaped)

    coolwarm_colors = matplotlib.cm.coolwarm_r

    fig.set_cmap(coolwarm_colors)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    return fig.get_size()


def parse_depth_image(snapshot):
    snapshot = json.loads(snapshot)

    user_id = snapshot["user_id"]
    snapshot_id = snapshot["snapshot_id"]

    width = snapshot["depth_image_width"]
    height = snapshot["depth_image_height"]
    path = snapshot["depth_image_path"]

    fig_height, fig_width = _prepare_fig(width, height, path)

    img_dir = f"{BASE_IMG_DIR}/{user_id}/{snapshot_id}"
    FSHandler.safe_create_dir(img_dir)
    img_path = f"{img_dir}/depth_img.png"
    #plt.savefig(img_path, bbox_inches="tight", transparent=True)
    plt.savefig(img_path)
    return dict(data_path=img_path, image_width=fig_width, image_height=fig_height)


parse_depth_image.scheme = 'depth_image'
