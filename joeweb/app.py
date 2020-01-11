"""
Holds the base class that puts all the pieces together
providing a symple interface for programming
"""

from joeweb.router import Router, Path
from joeweb.response import Response, FileResponse, Http404
from joeweb.response import Request
import os

class App:
    def __init__(self):
        self.router = Router()
        self.static_dir = None  # holds the path where static files are stored
        self.static_path = None # specifies the url prefix for all incoming static file requests

    def set_static(self, static_path, static_dir):
        # function used to set static file related settings
        self.static_dir  = static_dir
        self.static_path = static_path
        
    
    def serve_static(self,request : Request):
        """A view to serve static files that is only added when the user sets the static variables"""
        new_path = request.path[len(self.static_path)::] # get the actual file path name 
        return FileResponse(request, os.path.join(self.static_dir, new_path))


    def set_routes(self, routes : list):
        # takes a list of Paths and add them to the app's router's list of routes
        for path in routes:
            self.router.add_route(path)

    def __call__(self, environ, start_response):
        # the wsgi callable
        try:
            request = Request(environ, start_response)
            # check if this request is directed at getting static files
            if self.static_path !=None and  request.path.startswith(self.static_path):
                response = self.serve_static(request)
                return response.make_response()
            else:
                func = self.router.get_route(request.path)
                if func is not None:
                    response: Response = func(request)
                    return response.make_response()  
                else:
                    print(f'route Not found : {request.path}')
        except Exception as e:
            print(e)

        response =  Http404(request)
        return response.make_response()