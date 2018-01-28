import pytest
from http import HTTPStatus
from network import server
from unittest.mock import Mock

# create a mock HTTP request handler object to replicate a request from a client
@pytest.fixture(scope="module")
def http_request_handler():
    return Mock(spec=server.ServerRequestHandler)

# group related tests in a class
# don't write the __init__ method for classes

class TestServerReturnStatusCodes:
    @pytest.fixture(params=["/index.xml"])
    def good_path(self, request):
        http_request_handler.path = request.param

    @pytest.mark.usefixtures("good_path")
    def test_do_get_good_path_return_OK(self, http_request_handler):
        server.ServerRequestHandler.do_GET(http_request_handler)
        http_request_handler.send_response.assert_called_with(HTTPStatus.OK)
        http_request_handler.send_error.assert_not_called() # error was not sent

    @pytest.fixture(params=["foo.txt", "index.xml",
                            "/index.xml/"])
    def bad_path(self, request):
        http_request_handler.path = request.param

    @pytest.mark.usefixtures("bad_path")
    def test_do_get_bad_path_return_NOT_FOUND(self, http_request_handler):
        server.ServerRequestHandler.do_GET(http_request_handler)
        http_request_handler.send_error.assert_called_with(HTTPStatus.NOT_FOUND)
        http_request_handler.send_response.assert_not_called() # good response was not sent