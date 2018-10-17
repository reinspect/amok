from http.server import HTTPServer, BaseHTTPRequestHandler
from variables import *
from msg import *

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
print("\nRunning on " + ip + ":" + str(port))
print(stopMsg)
try:
    httpd.serve_forever()
    if(close==True):
        raise
        #httpd.server_close()
except KeyboardInterrupt:
    httpd.server_close()
    print("\n\nServer Stopped\nThanks for using AMOK!\n")
except:
    httpd.server_close()
    print("\n\nServer Stopped\nThanks for using AMOK!\n") 