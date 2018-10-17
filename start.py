import os
from core.msg import *
from core.variables import *

print(chr(27) + '[2J')

print(logo)

os.system('python3 ./core/check.py')
if runInBg == 1:
	os.system('nohup python3 ./core/server.py &')
	print(bgMsg)
else:
	os.system('python3 ./core/server.py')