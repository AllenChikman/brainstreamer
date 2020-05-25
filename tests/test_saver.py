import pytest

from mindreader.saver import Saver


def test_saver_parser_result_pose(mock_database, data_dir):
    with open(data_dir / 'pose_parser_result.json', 'r') as f:
        pose_parser_result = f.read()

    saver = Saver('mockurl://localhost:20000')
    saver.save('pose', pose_parser_result)

    pose = mock_database['data']['topics']['pose']

    assert pose['translation']['x'] == 0.4873843491077423
    assert pose['translation']['y'] == 0.007090016733855009
    assert pose['translation']['z'] == -1.1306129693984985

    assert pose['rotation']['x'] == 0.9571326384559261
    assert pose['rotation']['y'] == -0.26755994585035286
    assert pose['rotation']['z'] == -0.021271118915446748
    assert pose['rotation']['w'] == 0.9571326384559261


def test_save_user_from_cli(mock_database, data_dir):
    with open(data_dir / 'user.json', 'r') as f:
        user_json = f.read()

    saver = Saver('mockurl://localhost:20000')
    saver.save('user', user_json)

    user = mock_database['user']

    assert user.user_id == 781
    assert user.username == "Yosi"
    assert user.birthday == 424244422
    assert user.gender == "female"


@pytest.fixture
def mock_database(monkeypatch):
    storage = {}

    class MockDatabase:
        def __init__(self, url):
            pass

        def insert_user(self, user):
            storage['user'] = user

        def insert_data(self, data):
            storage['data'] = data
    from mindreader import drivers
    monkeypatch.setattr(drivers, 'Database', MockDatabase)
    return storage
