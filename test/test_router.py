from joeweb.router import Router, Path

from unittest import TestCase

def func1(request):
    return 1

def func2(request):
    return 2

route_1 = Path('/', func1)
route_2 = Path('/2', func2)
routes = [route_1, route_2]

class TestRouter(TestCase):
    def test_create_router(self):
        router = Router()
        self.assertEqual(router.routes, [])
    def test_create_router_with_routes(self):
        
        router = Router(routes =routes)
        self.assertEqual(router.routes , routes)
        
    def test_router_set_route(self):
        router = Router()

        router.add_route(route_1)
        self.assertEqual(router.routes[0], route_1)

    

    def test_router_get_route(self):
        router = Router()
        router.add_route(route_1)
        self.assertEqual(router.get_route('/'), route_1.func)
    
        