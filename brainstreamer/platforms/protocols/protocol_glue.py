'''
this module ...
'''

from .cognition_json_protocol import cognition_json_protocol as cjsp
from brainstreamer.utils import my_util_functions as my_utils


def _snapshot_to_flat_dict(snapshot):
    d = dict()

    d["datetime"] = my_utils.epoch_to_date(snapshot.datetime, milisecs=True)

    d["pose_translation_x"] = snapshot.pose.translation.x
    d["pose_translation_y"] = snapshot.pose.translation.y
    d["pose_translation_z"] = snapshot.pose.translation.z

    d["pose_rotation_x"] = snapshot.pose.rotation.x
    d["pose_rotation_y"] = snapshot.pose.rotation.y
    d["pose_rotation_z"] = snapshot.pose.rotation.z
    d["pose_rotation_w"] = snapshot.pose.rotation.w

    d["color_image_width"] = snapshot.color_image.width
    d["color_image_height"] = snapshot.color_image.height
    # d["color_image_data"] = snapshot.color_image.data

    d["depth_image_width"] = snapshot.depth_image.width
    d["depth_image_height"] = snapshot.depth_image.height
    # d["depth_image_data"] = snapshot.depth_image.data

    d["feelings_hunger"] = snapshot.feelings.hunger
    d["feelings_thirst"] = snapshot.feelings.thirst
    d["feelings_exhaustion"] = snapshot.feelings.exhaustion
    d["feelings_happiness"] = snapshot.feelings.happiness

    return d


def _user_to_flat_dict(user):
    d = dict()

    d["user_id"] = user.user_id
    d["username"] = user.username
    d["birthday"] = user.birthday
    d["gender"] = user.gender

    return d


def get_arranged_dicts(user, snapshot):
    # User Preparation
    user_dict = _user_to_flat_dict(user)

    user_dict['gender'] = ['male', 'female', 'unknown'][user.gender]
    user_dict['birthday'] = my_utils.epoch_to_date(user.birthday, date_format="%d/%m/%Y")

    # Snapshot Preparation
    snapshot_dict = _snapshot_to_flat_dict(snapshot)

    snapshot_dict['snapshot_id'] = snapshot_id = my_utils.get_unique_id()
    snapshot_dict['user_id'] = user_id = user_dict["user_id"]

    image_dir_path = f'{cjsp.get_data_path()}/{user_id}/{snapshot_id}'
    snapshot_dict["color_image_path"] = f'{image_dir_path}/color_image.cjsp'
    snapshot_dict["depth_image_path"] = f'{image_dir_path}/depth_image.cjsp'

    return user_dict, snapshot_dict

