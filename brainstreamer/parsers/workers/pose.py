import json


def parse_pose(snapshot):
    snapshot = json.loads(snapshot)

    rotation = dict(
        x=snapshot["pose_rotation_x"],
        y=snapshot["pose_rotation_y"],
        z=snapshot["pose_rotation_z"],
        w=snapshot["pose_rotation_w"])

    translation = dict(
        x=snapshot["pose_translation_x"],
        y=snapshot["pose_translation_y"],
        z=snapshot["pose_translation_z"])

    return dict(rotation=rotation, translation=translation)


parse_pose.topic = 'pose'
