#!/usr/bin/env python3

import subprocess
import shutil as sh
import os

def ChangePermissions(file):
# Cambiar permisos de el archivo que haya en la variable file
	result = subprocess.run(['chmod','o+wx',file])
	if result.returncode != 0:
		print("No se lograron cambiar los permisos de el archivo " + file +  ". " + str(result))
		return False
	return True

def CopyFile(file):
# Copiar el archivo que haya en la variable fileDest a la ruta correcta
	destPath = os.path.realpath('../scripts/' + file)
	try:
		sh.copy(file, destPath)
		return(True)
	except Exception as e:
		print("No se logro copiar el archivo " + file + ". " + str(e))
		return(False)


def main():
	if not ChangePermissions('example.py'): exit()
	if not CopyFile('example.py'): exit()
	


if __name__ == "__main__":
	main()
