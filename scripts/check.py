import os
from variables import *

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
	indexTemplate = open('./templates/index.html', 'r')
	indexHtml = indexTemplate.read()

	newIndex = open(publicDir + indexFile ,"w+")
	newIndex.write(indexHtml)
	
	newIndex.close()
	indexTemplate.close()

#
# Check if Error File Exists
#

if os.path.exists(errorDir + error404):
	print('Error File exists [✔]')
else:
	print('Creating Error File [' + errorDir + error404 + ']')
	errorTemplate = open('./templates/404.html', 'r')
	errorHtml = errorTemplate.read()

	newError = open(errorDir + error404 ,"w+")
	newError.write(errorHtml)
	
	newError.close()
	errorTemplate.close()