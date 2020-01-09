from unittest import TestCase
from test.utils import environ, start_response
from src.request import Request
from src.response import Response

class Testresponse(TestCase):
    def test_reponse_created(self):
        print('running')
        request = Request(environ, start_response)
        response = Response(request, '200 OK', 'text/html')
        self.assertEqual(response.headers, [])
        self.assertEqual(response.status_code, '200 OK')
        self.assertEqual(response.content_type ,'text/html' )
        self.assertEqual(response.response_content, [])