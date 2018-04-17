import psutil
print("disc partitions:")
print(psutil.disk_partitions())
print("disc usage:")
print(psutil.disk_usage('/'))
print("disc io_counter:")
print(psutil.disk_io_counters(perdisk=False))
