import pytest

from brainstreamer.saver import Saver


def test_saver_parser_result_pose(mock_database, data_dir):
    with open(data_dir / 'translation_res.json', 'r') as f:
        pose_res = f.read()

    saver = Saver('mockurl://localhost:20000')

    saver.save('pose', pose_res)

    res = mock_database['results']['topics']['pose']

    assert res['translation']['x'] == 1.1
    assert res['translation']['y'] == -2.2
    assert res['translation']['z'] == 3.333


def test_save_user_from_cli(mock_database, data_dir):
    with open(data_dir / 'user.json', 'r') as f:
        user_json = f.read()

    saver = Saver('mock://localhost:20000')
    saver.save('user', user_json)

    user_dict = mock_database['user']

    assert user_dict["user_id"] == 78
    assert user_dict["username"] == "Allen"
    assert user_dict["birthday"] == 808448901
    assert user_dict["gender"] == "male"


@pytest.fixture
def mock_database(monkeypatch):
    storage = {}

    class MockDatabase:
        def __init__(self, url):
            pass

        def insert_user(self, user):
            storage['user'] = user

        def insert_results(self, data):
            storage['results'] = data

    def mock_init(self, database_url):
        self.db = MockDatabase(database_url)

    monkeypatch.setattr(Saver, '__init__', mock_init)
    return storage
