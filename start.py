import os
from scripts.signs import *
from scripts.variables import *

print(chr(27) + '[2J')

print(logo)

os.system('python3 ./scripts/check.py')
if runInBg == 1:
	os.system('nohup python3 ./scripts/server.py &')
	print(bgMsg)
else:
	os.system('python3 ./scripts/server.py')

print("Click Enter/Return...")