import os
import shutil

path = '此电脑\\Honor 8\\内部存储'
for root, dirs, files in os.walk(path):
    for f in files:
    	print(path,root)
    	pp = os.path.join(root, f)
    	print (pp)
    	if pp not in path:
	        # shutil.move(pp, path)
	        print("move %s -> %s" % (pp, path))
