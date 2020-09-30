#!/usr/bin/env python3

import subprocess
import shutil as sh
import os

def ChangePermissions():
# Cambiar permisos de example.py
	result = subprocess.run(['chmod','o+wx','example.py'])
	if result.returncode != 0:
		print("No se lograron cambiar los permisos de el archivo example.py. " + str(result))
		return False
	return True

def CopyFile():
# Copiar example.py a la ruta correcta
	destPath = os.path.realpath('../scripts/example.py')
	try:
		sh.copy("example.py", destPath)
		return(True)
	except Exception as e:
		print("No se logro copiar el archivo example.py. " + str(e))
		return(False)


def main():
	if not ChangePermissions(): exit()
	if not CopyFile(): exit()
	


if __name__ == "__main__":
	main()
