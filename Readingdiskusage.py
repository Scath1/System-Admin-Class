import psutil

print psutil.disk_partitions()


print psutil.disk_usage("/cd/home/pi/Desktop)


print psutil.disk_io_counters(perdisk=True)