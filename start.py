import os
from logo import *

print(chr(27) + "[2J")

print(logo)

if os.path.exists('./public'):
	print("Public exists")
else:
	print("Public existsn't")