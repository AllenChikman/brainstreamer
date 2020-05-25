import pytest
import requests
from brainstreamer.client import run as upload_sample
from brainstreamer.platforms.protocols.cogintion_pb_protocol import cognition_pb_protocol as pb


def test_trivial():
    pass


def test_send_snapshot(data_dir, requests_post_data):
    sample = data_dir / 'snapshot.gz'

    num_of_snaps_to_read = 1
    upload_sample('127.0.0.1', 42652, num_of_snaps_to_read ,sample)

    message = requests_post_data[0]
    user, snapshot = pb.deserialize_message(message)

    assert user.user_id == 42
    assert user.username == 'Dan Gittik'
    assert snapshot.feelings.happiness == 0
    assert snapshot.pose.rotation.x == -0.10888676356214629
    # assert snapshot.pose.translation.x == 0.4873843491077423


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

# def test_sample_file_not_exist(tmp_path):
#     sample = tmp_path / 'invalid_sample'
#
#     with pytest.raises(FileNotFoundError):
#         upload_sample('127.0.0.1', 42652, sample)
#
#
# def test_invalid_server(data_dir):
#     sample = data_dir / 'snapshot.gz'
#
#     with pytest.raises(ConnectionRefusedError):
#         upload_sample('127.0.0.1', 42652, sample)
