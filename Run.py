import os

fileName = "Main.py"

os.system('chmod a+wxr {0}'.format(fileName))
os.system('python3 {0}'.format(fileName))
