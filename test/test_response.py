from unittest import TestCase
from test.utils import environ, start_response
from joeweb.request import Request
from joeweb.response import Response, HttpResponse, Http404

class Testresponse(TestCase):
    def test_reponse_created(self):
        request = Request(environ, start_response)
        response = Response(request, '200 OK', 'text/html')
        self.assertEqual(response.headers, [])
        self.assertEqual(response.status_code, '200 OK')
        self.assertEqual(response.content_type ,'text/html' )
        self.assertEqual(response.response_content, [])
    
    def test_http_response(self):
        request = Request(environ, start_response)
        http_response = HttpResponse(request, 'Hello world')
        self.assertIsInstance(http_response.response_content, list)
        self.assertEqual(http_response.make_response(), [b'Hello world'])
    