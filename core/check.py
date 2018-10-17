import os
from variables import *
from templates import *

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