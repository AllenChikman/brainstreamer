import pytest
import requests
from mindreader.client import upload_sample
from mindreader.drivers import Encoder


def test_sample_file_not_exist(tmp_path):
    sample = tmp_path / 'invalid_sample'

    with pytest.raises(FileNotFoundError):
        upload_sample('127.0.0.1', 42652, sample)


def test_invalid_server(data_dir):
    sample = data_dir / 'snapshot.gz'

    with pytest.raises(ConnectionRefusedError):
        upload_sample('127.0.0.1', 42652, sample)


def test_send_snapshot(data_dir, requests_post_data):
    sample = data_dir / 'snapshot.gz'

    upload_sample('127.0.0.1', 42652, sample)

    encoder = Encoder('protobuf')

    message = requests_post_data[0]
    user, snapshot = encoder.message_decode(message)

    assert user.user_id == 42
    assert user.username == 'Dan Gittik'
    assert snapshot.feelings.happiness == 0
    assert snapshot.pose.translation.x == 0.4873843491077423
    assert snapshot.pose.rotation.x == 0.9571326384559261


@pytest.fixture
def requests_post_data(monkeypatch):
    post_message = []

    def mock_post(url, data):
        post_message.append(data)
        return MockResponse()

    class MockResponse:
        status_code = 200

    monkeypatch.setattr(requests, 'post', mock_post)
    return post_message
