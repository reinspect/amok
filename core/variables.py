import json

with open('config.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

ip = data['ip']
port = data['port']
runInBg = data['runInBackground']
publicDir = data['publicDir']
errorDir = data['errorDir']
indexFile = data['indexFile']
error404 = data['error404']