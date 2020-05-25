import os
import pytest
import json

from brainstreamer.parsers import parse


@pytest.fixture
def json_snapshot(data_dir):
    with open(data_dir / 'snapshot.json', 'r') as f:
        raw_snapshot = f.read()
    return raw_snapshot


@pytest.fixture
def flat_dict_snapshot(data_dir):
    with open(data_dir / 'processed_snapshot_raw.json', 'r') as f:
        snapshot = f.read()
    return snapshot


def test_parse_pose(flat_dict_snapshot):
    json_parsing_result = parse('pose', flat_dict_snapshot)
    parsing_result = json.loads(json_parsing_result)

    print(parsing_result)
    assert parsing_result['translation']['x'] == 0.123
    assert parsing_result['translation']['y'] == 0.456
    assert parsing_result['translation']['z'] == 0.789

    assert parsing_result['rotation']['w'] == 0
    assert parsing_result['rotation']['x'] == 0.123
    assert parsing_result['rotation']['y'] == 0.456
    assert parsing_result['rotation']['z'] == 0.789


def test_parse_feelings(flat_dict_snapshot):
    json_parsing_result = parse('feelings', flat_dict_snapshot)
    parsing_result = json.loads(json_parsing_result)

    assert parsing_result['hunger'] == 1.0
    assert parsing_result['thirst'] == -0.5
    assert parsing_result['exhaustion'] == 0
    assert parsing_result['happiness'] == 0.23434


def test_parse_pose_from_cli(data_dir, tmp_path):
    source_path = data_dir / 'processed_snapshot_raw.json'
    result_path = f'{tmp_path}/pose.result'
    command = f"python -m brainstreamer.parsers parse 'pose' {source_path} > {result_path}"
    os.system(command)

    with open(result_path, 'r') as f:
        json_parsing_result = f.read()
    parsing_result = json.loads(json_parsing_result)

    assert parsing_result['translation']['x'] == 0.123
    assert parsing_result['translation']['y'] == 0.456
    assert parsing_result['translation']['z'] == 0.789

    assert parsing_result['rotation']['w'] == 0
    assert parsing_result['rotation']['x'] == 0.123
    assert parsing_result['rotation']['y'] == 0.456
    assert parsing_result['rotation']['z'] == 0.789
