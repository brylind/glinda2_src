import os
import time

time.sleep(30)
os.system("cd /home/pi/Documents/Github/GLINDA2_testing && git pull")
os.system("echo Git Pull completed!")