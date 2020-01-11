from unittest import TestCase
from joeweb.app import App
from joeweb.router import Router

from joeweb.response import Response, Http404
from test.utils import environ, start_response

def static_func(*args):
    return 'called'
class Testapp(TestCase):
    def test_create_app(self):
        app = App()
        self.assertEqual(app.static_dir, None)
        self.assertEqual(app.static_path, None)
        self.assertIsInstance(app.router, Router)
        self.assertEqual(len(app.router.routes), 0)

    def test_set_static(self):
        app = App()
        app.set_static('/static','static_folder')
        self.assertEqual(app.static_dir, 'static_folder')
        self.assertEqual(app.static_path, '/static')
        self.assertEqual(len(app.router.routes), 0)
    
    def test_called(self):
        env = environ.copy()
        env['PATH_INFO'] = '/'
        app = App()
        self.assertIsInstance(app(environ, start_response), list)
    def test_called_with_non_existent_route(self):
        env = environ.copy()
        env['PATH_INFO'] = '/does/not/exist/'
        app = App()
        self.assertEqual(app(environ, start_response), [b'404 Not Found'])
        