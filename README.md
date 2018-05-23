# Prepared Python Scripts
* Unless otherwise stated Python version used is 3.6.3.
* Purpose of these scripts is to help me develop my Python development skills and prevent re-write of boiler plate code in projects that I work on.

## web_server_gateway_interface.py
The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python.

The example python in this file allows a developer to quickly get a python WSGI up and running with minimal effort. The file also contains examples of how to handle simple http GET and POST requests.

For further details see [wsgiref docs](https://docs.python.org/3/library/wsgiref.html)

#### Steps to run
* wsgiref comes installed as a standard Python 3 package, no pip install.
* Run `python web_server_gateway_interface.py` in the terminal to start the WSGI. You should see "Serving on Port 8002" printed to the terminal.
* Visit [localhost:8002](http://localhost:8002/) to ensure the WSGI is up and running. You should see "This is a GET request" returned to the window.
