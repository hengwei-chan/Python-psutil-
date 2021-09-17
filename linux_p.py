import  psutil
import os
for proc in psutil.process_iter():
    if (proc.username()=='xxx'):
        os.system("sudo renice -20 -p %s "%(proc.pid))
