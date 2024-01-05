# Runs on Python 3.8+
# Code for the article https://itnext.io/pem-file-basics-with-mkcert-and-docker-07a7b99d9353
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        certfile='dev.localhost.pem',
        keyfile='dev.localhost-key.pem',
        server_side=True)

httpd.serve_forever()