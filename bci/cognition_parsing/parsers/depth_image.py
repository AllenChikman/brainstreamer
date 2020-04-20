import json
import numpy
import matplotlib
import matplotlib.pyplot as plt
from bci.utils import FileSystemHandler as FSH
import logging

logger = logging.getLogger(__name__)

def parse_depth_image(snapshot):
    snapshot = json.loads(snapshot)
    width = snapshot["depth_image_width"]
    height = snapshot["depth_image_height"]
    path = snapshot["depth_image_path"]

    size = height, width
    data = FSH.load(path, byte=True)
    data = json.loads(data)

    shaped = numpy.reshape(data, size)
    fig = plt.imshow(shaped, cmap='hot', interpolation='nearest')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig("/home/user/brain-computer-interface/bci/protocols/shared_data/42/depth_pic")
    return json.dumps({'data_path': path, 'image_width': width, 'image_height': height})


parse_depth_image.field = 'depth_image'
