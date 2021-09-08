import time,os,shutil


source = "C:/Users/Ranvi/Desktop/python2/p20"

days = 2
seconds = time.time()-(days*24*60*60)
allfiles = os.listdir(source)
for i in allfiles:
    filepath = os.path.join(source,i)
    if os.stat(filepath).st_mtime < seconds:
        if os.path.isdir(filepath):
            shutil.rmtree(filepath)
        elif os.path.isfile(filepath):
            os.remove(filepath)    



