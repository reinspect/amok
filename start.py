import os
from logo import *
from variables import *

print(chr(27) + "[2J")

print(logo)

if os.path.exists(publicDir):
	print("Public Directory exists [✔]")
else:
	print("Creating Public Directory [" + publicDir + "]")
	os.makedirs(publicDir)

if os.path.exists(errorDir):
	print("Error Directory exists [✔]")
else:
	print("Creating Error Directory [" + errorDir + "]")
	os.makedirs(errorDir)