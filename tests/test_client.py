import pytest
import requests
from brainstreamer.client import run as upload_sample
from brainstreamer.platforms.protocols import client_server_protocol


def test_one_more_green_point_for_good_feeling():
    assert True


def test_send_snapshot(data_dir, requests_post_data):
    sample = data_dir / 'snapshot.gz'
    print(sample)
    # sample = "./brainstreamer/data/sample.mind.gz"
    num_of_snaps_to_read = 1
    upload_sample('127.0.0.1', 12345, num_of_snaps_to_read, sample)

    message = requests_post_data[0]
    user, snapshot = client_server_protocol.deserialize_message(message)

    assert user.user_id == 42
    assert user.username == 'Dan Gittik'
    assert snapshot.feelings.happiness == 0
    assert snapshot.pose.rotation.x == -0.10888676356214629


@pytest.fixture
def requests_post_data(monkeypatch):
    post_message = []

    class MockResponse:
        status_code = 200

    def mock_post(url, data):
        post_message.append(data)
        return MockResponse()

    monkeypatch.setattr(requests, 'post', mock_post)
    return post_message


