from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def make_ben_a_server(environ, start_response):

    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']

    print(path)
    print(method)
    
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

# Create a webserver on local host on port 8002
with make_server('', 8002, make_ben_a_server) as httpd:
    print("Serving on Port 8002")

    # Serve until process is killed
    httpd.serve_forever()
