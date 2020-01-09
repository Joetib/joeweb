from src.router import Router

from unittest import TestCase

def func1(request):
    return 1

def func2(request):
    return 2

class TestRouter(TestCase):
    def test_create_router(self):
        router = Router()
        self.assertEqual(router.routes, {})
    def test_create_router_with_routes(self):
        router = Router(routes = {'/': func1, '/2': func2})
        self.assertEqual(router.routes , {'/': func1, '/2': func2})
        
    def test_router_set_route(self):
        router = Router()
        router.add_route('/', func1)
        self.assertEqual(router.routes['/'], func1)

    def test_set_two_routes_with_same_path(self):
        router = Router()
        router.add_route('/', func1)
        router.add_route('/', func2)
        self.assertNotEqual(router.get_route('/'), func1)
        self.assertEqual(router.get_route('/'), func2)


    def test_router_get_route(self):
        router = Router()
        router.add_route('/', func1)
        self.assertEqual(router.get_route('/'), func1)
    
        