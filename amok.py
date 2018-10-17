import os
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler

#
# Configuration
#

ip = "127.0.0.1"
port = 8000
runInBg = 1
publicDir = "./public/www/"
errorDir = "./public/error/"
indexFile = "index.html"
error404 = "404.html"

#
# source: msg.py
#

logo = """
 █████╗ ███╗   ███╗ ██████╗ ██╗  ██╗
██╔══██╗████╗ ████║██╔═══██╗██║ ██╔╝
███████║██╔████╔██║██║   ██║█████╔╝ 
██╔══██║██║╚██╔╝██║██║   ██║██╔═██╗ 
██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██╗
╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
AMOK - amok.reinspect.org
"""

stopMsg = """
+----------------------------+
| Press [CTRL] + [C] to stop |
+----------------------------+
"""

bgMsg = """
+-----------------------------------+
| AMOK is running in the Background |
+-----------------------------------------+
| To Stop it, type: python3 amok.py -stop |
+-----------------------------------------+
"""

killMsg = """
+-----------------------+
| AMOK has been stopped |
+-----------------------+
"""

parser = argparse.ArgumentParser(description="stops AMOK")
parser.add_argument('-stop', action='store_true')
parser.add_argument('-server', action='store_true')

args = parser.parse_args()

if args.stop:
	os.system('pkill -f amok.py')
	print(killMsg)
	exit()
if args.server:
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
    httpd.serve_forever()

print(chr(27) + '[2J')

print(logo)

#
# source: templates.py
#

indexTemp = """
<!DOCTYPE html>
<html>

<head>
    <title>Welcome!</title>
    <style type="text/css">
    * {
        font-family: Helvetica Neue, sans-serif;
        color: #0f0f0f;
    }

    html,
    body {
        margin: 0;
    }

    div.flex {
        display: flex;
        width: 100vw;
        height: 100vh;
        align-items: center;
        justify-content: center;
    }

    div.box {
        display: block;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 10px;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    p {
        margin: 0;
    }

    h1.title {
        text-align: center;
        margin-bottom: 10px;
    }

    hr {
        height: 1px;
        background: #ddd;
        border: none;
    }
    </style>
</head>

<body>
    <div class="flex">
        <div class="box">
            <h1 class="title">Welcome to my Website!</h1>
            <hr>
            <p>This is a brand new spanking website ran by a Python Web Server!</p>
            <hr>
            <p><a href="https://github.com/reinspect/amok">Amok</a></p>
        </div>
    </div>
</body>

</html>
"""

errorTemp = """
<!DOCTYPE html>
<html>

<head>
    <title>Page not found!</title>
    <style type="text/css">
    * {
        font-family: Helvetica Neue, sans-serif;
        color: #0f0f0f;
    }

    html,
    body {
        margin: 0;
    }

    div.flex {
        display: flex;
        width: 100vw;
        height: 100vh;
        align-items: center;
        justify-content: center;
    }

    div.box {
        display: block;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 10px;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    p {
        margin: 0;
    }

    h1.title {
        text-align: center;
        margin-bottom: 10px;
    }

    hr {
        height: 1px;
        background: #ddd;
        border: none;
    }
    </style>
</head>

<body>
    <div class="flex">
        <div class="box">
            <h1 class="title">404</h1>
            <hr>
            <p>Page is not found!</p>
            <hr>
            <p><a href="https://github.com/reinspect/amok">Amok</a></p>
        </div>
    </div>
</body>

</html>
"""

#
# source: check.py
#

#
# Check if Public Directory Exists
#

if os.path.exists(publicDir):
    print('Public Directory exists [✔]')
else:
    print('Creating Public Directory [' + publicDir + ']')
    os.makedirs(publicDir)

#
# Check if Error Directory Exists
#

if os.path.exists(errorDir):
    print('Error Directory exists [✔]')
else:
    print('Creating Error Directory [' + errorDir + ']')
    os.makedirs(errorDir)

#
# Check if Index File Exists
#

if os.path.exists(publicDir + indexFile):
    print('Index File exists [✔]')
else:
    print('Creating Index File [' + publicDir + indexFile + ']')
    newIndex = open(publicDir + indexFile ,"w+")
    newIndex.write(indexTemp)
    
    newIndex.close()

#
# Check if Error File Exists
#

if os.path.exists(errorDir + error404):
    print('Error File exists [✔]')
else:
    print('Creating Error File [' + errorDir + error404 + ']')

    newError = open(errorDir + error404 ,"w+")
    newError.write(errorTemp)
    
    newError.close()

#
# source: server.py
#

if runInBg == 1:
    os.system('nohup python3 amok.py -server &')
    print(bgMsg)
else:
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