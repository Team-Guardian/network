from network import server
from unittest.mock import Mock
# We want to test if what do_GET function does meets our expectations
# For example, if a directory listing is requested, how does do_GET respond?

# Tests for which you need to substitute 'self' varaible 
# with a custom one
# for example, self.path is modified to a custom filepath
# and at the end the function that makes a full path is
# tested for whether it correctly formed the path using self.path

class TestServer:
    # don't write the __init__ method
    
    def setup(self):
        self.mock_http_request_handler = Mock(spec=server.ServerRequestHandler)

    def test_do_get_response_code_200(self):
        server.ServerRequestHandler.do_GET(self.mock_http_request_handler)
        self.mock_http_request_handler.send_response.assert_called_with(200)