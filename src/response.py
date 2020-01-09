from .request import Request


class Response:

    """
    Base Response Class
    """
    __slots__ = 'headers', 'status_code', 'start_response', 'content_type', 'response_content'

    def __init__(self,request: Request, status_code: str, content_type: str):
        self.headers = []
        self.status_code = status_code
        self.start_response = request.start_response
        self.content_type = content_type
        self.response_content = []
        return self

    def make_response(self):
        self.start_response(self.status_code, [('Content-Type', self.content_type)])
        return self.response_content
            

    def __iter__(self):
        for i in self.response_content:
            yield i
            


class HttpResponse(Response):
    """
    Return pure http response when given a text as content
    """
    def __init__(self, request: Request, content: str, status_code='200 OK', content_type='text/html'):
        super().__init__( request, status_code, content_type)
        self.response_content.append(content.encode())

class RenderResponse(HttpResponse):

    """Uses HttpResponse to return pure http response"""


    def __init__(self, request: Request, filename: str, context: dict):
        try:
            with open(filename, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f'Error openning file {filename}')
            raise Exception(f'Could not find the file {filename}')
        text.format(context)
        super().__init__(request, text, '200 OK')


class JsonResponse(Response):
    """
    Return pure json response when given a text as content
    """
    def __init__(self, request: Request, content, status_code='200 OK', content_type='application/json'):
        import json
        content = json.dumps(content)
        super().__init__( request, status_code, content_type)
        self.response_content.append(content.encode())

class FileResponse(HttpResponse):
    def __init__(self,  request: Request, filename: str, file_root:str=""):
        try:
            with open(file_root+filename, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f'File not found {filename}')
            raise Exception(f'could not find the file {filename}')
        if filename.endswith('.html') or filename.endswith('.htm'):
            content_type = 'text/html'
        elif filename.endswith('.css'):
            content_type = 'text/css'
        elif filename.endswith('.js'):
            content_type = 'text/javascript'
        
        super().__init__( request, text, '200 OK',content_type )

class MemoryFileResponse(HttpResponse):
    def __init__(self, request:Request, data):
        super().__init__(request, data, '200 OK', '')

class ErrorResponse(Response):
    def __init__(self, request: Request, error_code: str):
        super().__init__(request, '404 Not Found', 'text/html')
        self.response_content.append("404 Not Found".encode())


class Http404(ErrorResponse):
    def __init__(self, request):
        super().__init__(request, '404 Not Found')

