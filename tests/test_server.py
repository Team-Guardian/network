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
    @pytest.fixture()
    def good_path(self, http_request_handler):
        http_request_handler.path = "/"

    @pytest.mark.usefixtures("good_path")
    def test_do_get_good_path_return_OK(self, http_request_handler):
        server.ServerRequestHandler.do_GET(http_request_handler)
        http_request_handler.send_response.assert_called_with(HTTPStatus.OK)
        http_request_handler.send_error.assert_not_called() # error was not sent

    @pytest.fixture(params=["must_fail_test.txt", "/must_fail_test"])
    def bad_path(self, http_request_handler, request):
        http_request_handler.path = request.param

    @pytest.mark.usefixtures("bad_path")
    def test_do_get_bad_path_return_NOT_FOUND(self, http_request_handler):
        server.ServerRequestHandler.do_GET(http_request_handler)
        http_request_handler.send_error.assert_called_with(HTTPStatus.NOT_FOUND)

class TestResponseHeaderGenerator:
    @pytest.mark.parametrize("extension, expected_content_type", [
            ("foo.jpg", "image/jpeg"),
            ("foo.jpeg", "image/jpeg"),
            ("foo.txt", "text/plain"),
    ])
    def test_sendHeaders_content_type(self, http_request_handler, extension, expected_content_type):
        http_request_handler.path = extension
        server.ServerRequestHandler.sendHeaders(http_request_handler)
        http_request_handler.send_header.assert_called_with('Content-type', expected_content_type)
        http_request_handler.end_headers.assert_called() # don't forget to explicitly stop sending headers