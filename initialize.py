#!/usr/bin/env python3

import shutil as sh
import os

destPath = os.path.realpath('../scripts/example.py')
print(destPath)
sh.copy("example.py", + destPath)
#print(result)
