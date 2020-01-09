"""
Holds the base class that puts all the pieces together
providing a symple interface for programming
"""

from .router import Router, Path
from .response import Response, FileResponse, Http404
from .response import Request

class App:
    def __init__(self):
        self.router = Router()
        self.static_dir = None
        self.static_path = None

    def set_static(self, static_path, static_dir):
        self.static_dir  = static_dir
        self.static_path = static_path
        self.router.add_route(Path(self.static_path, self.serve_static))
    
    def serve_static(self,request : Request):
        """A view to serve static files that is only added when the user sets the static variables"""
        new_path = request.path[len(self.static_path)::] # get the actual file path name 
        return FileResponse(request, new_path)


    def set_routes(self, routes : list):
        for path in routes:
            self.router.add_route(path)
        return True

    def __call__(self, environ, start_response):
        request = Request(environ, start_response)
        if self.static_path !=None and  request.path.startswith(self.static_path):
            response = self.serve_static(request)
            return response.make_response()
        else:
            try:
                func = self.router.get_route(request.path)
                response: Response = func(request)
                return response.make_response()
            except Exception as e:
                print(e, '\n Exception while executing request')
                response =  Http404(request)
                return response.make_response()