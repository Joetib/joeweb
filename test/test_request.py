from src.request import Request
from unittest import TestCase
from test.utils import start_response, environ


class Testrequest(TestCase):
    def test_create_request(self):
        request = Request(environ, start_response)
        self.assertEqual(request.http_host , environ['HTTP_HOST'])
        self.assertEqual(request.http_user_agent , environ['HTTP_USER_AGENT'])
        self.assertEqual(request.lang , environ.get('LANG'))
        self.assertEqual(request.method , environ.get('REQUEST_METHOD'))
        self.assertEqual(request.path , environ.get('PATH_INFO'))
        self.assertEqual(request.host_address , environ.get('HTTP_HOST'))
        self.assertEqual(request.gateway_interface , environ.get('GATEWAY_INTERFACE'))
        self.assertEqual(request.server_port , environ.get('SERVER_PORT'))
        self.assertEqual(request.remote_host , environ.get('REMOTE_HOST'))
        self.assertEqual(request.content_length , environ.get('CONTENT_LENGTH'))
        self.assertEqual(request.server_protocol , environ.get('SEVER_PROTOCOL'))
        self.assertEqual(request.server_software , environ.get('SERVER_SOFTWARE'))
        self.assertEqual(request.start_response , start_response)
        self.assertEqual(request.environ , environ)
