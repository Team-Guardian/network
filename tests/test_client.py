import pytest
import http.client
from http import HTTPStatus
from network import client
from unittest.mock import Mock

@pytest.fixture(scope="module")
def http_connection():
    return Mock(spec=http.client.HTTPConnection)

@pytest.fixture(scope="module")
def http_response():
    return Mock(spec=http.client.HTTPResponse)

@pytest.fixture(scope="module")
def http_client():
    return Mock(spec=http.client)

class TestClientImageTransfer:
    @pytest.fixture()
    def get_resource_NOT_FOUND(self, http_response):
        http_response.status = HTTPStatus.NOT_FOUND

    @pytest.fixture()
    def get_image_OK(self, http_response):
        http_response.status = HTTPStatus.OK
    
    @pytest.fixture()
    def save_image_mock(self):
        return Mock(spec=client.saveImage)

    # check if client saves image after receiving it
    @pytest.mark.usefixtures("get_image_OK")
    def test_received_image_saved_on_disk(self, save_image_mock, monkeypatch):
        monkeypatch.setattr(client, "saveImage", save_image_mock)
        client.getImage("foo.jpg")
        save_image_mock.assert_called()