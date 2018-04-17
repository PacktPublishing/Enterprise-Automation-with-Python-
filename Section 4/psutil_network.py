import psutil

print("net_io_counters", psutil.net_io_counters(pernic=True))

print("net_if_addrs:", psutil.net_if_addrs())

print("net_if_stats:", psutil.net_if_stats())

