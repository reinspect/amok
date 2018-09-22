from http.server import HTTPServer, BaseHTTPRequestHandler
from variables import *

class httpServe(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(publicDir + self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = open(errorDir + '404.html').read()
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer((ip, port), httpServe)
httpd.serve_forever()