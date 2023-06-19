import psutil

print('CPU usage is {0}'.format(psutil.cpu_percent(5)))

print('memory usage is {0}'.format(psutil.virtual_memory()))
