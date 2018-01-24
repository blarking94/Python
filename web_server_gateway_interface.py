#################################################################################################
#                                                                                               #
# File Name     - web_server_gateway_interface.py                                               #
# Author        - Ben Larking                                                                   #
# Date Created  - 22/01/2018                                                                    #
# Date Modified - 24/01/2018                                                                    #
# Description   - Basic WSGI for a python application, gives an example of how to handle        #
#                 a POST or GET request and pull out any query strings.                         #
#                                                                                               #
#################################################################################################

from wsgiref.simple_server import make_server

ok_status = '200 OK'

# Basic successful headers
def get_basic_response_headers(response_body):
    return [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

# Convert any variables passed in the query to a dict
def extract_query_variables_to_dict(query_string):
    get_dict = {}
    for param in query_string.split('&'):
        key, value = (param.split('=')) if (len(param.split('='))) > 1 else (None, None)
        get_dict[key] = value
    return get_dict


def make_a_server(environ, start_response):

    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']

    # Defaults set to '/' and GET
    print(path)
    print(method)

    response_body = b""

    if method == 'POST':

        # if path is localhost:8002/me send back basic POST message,
        # if there are variables i.e localhost:8002/me?name=ben show these variables
        if path.startswith('/me'):
            response_body = ("You posted me! %s" % (extract_query_variables_to_dict(environ['QUERY_STRING']))).encode("utf-8")
        else:
            response_body = b"This is a POST request"

        start_response(ok_status, get_basic_response_headers(response_body))

    elif method == 'GET':

        # if path is localhost:8002/me send back basic GET message,
        # if there are variables i.e localhost:8002/me?name=ben show these variables
        if path.startswith('/me'):
            response_body = ("You got me! %s" % (extract_query_variables_to_dict(environ['QUERY_STRING']))).encode("utf-8")
        else:
            response_body = b"This is a GET request"

        start_response(ok_status, get_basic_response_headers(response_body))
    else:
        response_body = ("Currently %s is an unsupported method, try POST or GET." % (method)).encode("utf-8")
        start_response(ok_status, get_basic_response_headers(response_body))


    # The returned object is going to be printed
    return [response_body]

# Create a webserver on local host on port 8002
with make_server('', 8002, make_a_server) as httpd:
    print("Serving on Port 8002")

    # Serve until process is killed
    httpd.serve_forever()
