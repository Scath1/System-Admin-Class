import psutil
import time


ans=True

while ans:
	time.sleep(10)


	print psutil.virtual_memory().percent
	

	print psutil.virtual_memory()




