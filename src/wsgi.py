

from wsgiref.simple_server import make_server



def app(environ, start_response):
    
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello world']


if __name__=='__main__':
    server = make_server('127.0.0.1', 80, app)
    server.serve_forever()

