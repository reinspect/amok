import os
from scripts.logo import *

print(chr(27) + '[2J')

print(logo)

os.system('python3 ./scripts/check.py')
os.system('python3 ./scripts/server.py')