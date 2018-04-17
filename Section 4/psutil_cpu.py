import psutil

print("cpu times: ", psutil.cpu_times())

for x in range(3):
    print("cpu percent: ", psutil.cpu_percent(interval=1))

for x in range(3):
    print("cpu percent per cpu core: ", psutil.cpu_percent(interval=1, percpu=True))

for x in range(3):
    print("cpu times percent: ", psutil.cpu_times_percent(interval=1, percpu=False))

print("cpu count:", psutil.cpu_count())
print("cpu count physical: ", psutil.cpu_count(logical=False))
print("cpu stats: ", psutil.cpu_stats())
print("cpu freq: ", psutil.cpu_freq())
