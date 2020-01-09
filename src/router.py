
class Path:
    """
    Class to hold paths. makes it easier to check matches
    """

    __slots__ = 'path', 'func'

    def __init__(self, _path: str, _func):
        self.path = _path
        self.func = _func

    
    def match(self, _path):
        if self.path == _path:
            return True
        return False
    

class Router:
    """
    Holds all routes in a list. When connection comes it is used to check which of those
    paths match the url
    """
    __slots__ = 'routes'
    def __init__(self, routes:list=None):
        self.routes:list = list(routes) if routes else []

    def add_route(self,  _path: Path):
        self.routes.append(_path)
        return True
        

    def get_route(self, path_):
        for path in self.routes:
            if path.match(path_):
                return path.func
        print(f'{path_}')
        raise Exception('Route not found')


