import json
from mindreader.drivers.context import Context
import numpy
import matplotlib
import matplotlib.pyplot as plt


def parse_depth_image(snapshot):
    snapshot = json.loads(snapshot)
    size = snapshot["depth_image_height"], snapshot["depth_image_width"]
    path = snapshot["depth_image_path"]
    # TODO: maybe use the path?
    context = Context.generate_from_snapshot(snapshot)
    data = json.loads(context.load('depth_image'))
    shaped = numpy.reshape(data, size)
    fig = plt.imshow(shaped)
    fig.set_cmap(matplotlib.cm.RdYlGn)  # TODO: cmap=hot, interpolation='nearest'?
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    height, width = fig.get_size()
    # print(plt.get_size_inches())
    # plt.colorbar()

    image_path = context.path('depth_image.png')
    plt.savefig(image_path)
    return json.dumps({'data_path': image_path, 'image_width': width, 'image_height': height})


parse_depth_image.field = 'depth_image'
