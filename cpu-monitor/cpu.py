__author__ = 'avniAayush'

import psutil
import csv
import time

def csv_write(data):
    #import pdb;pdb.set_trace()
    for row in data:
        out.write('%s;' %row)
    out.write('\n')
    #out.close()

out = open('out.csv', 'w')
writer = csv.writer(out)
writer.writerow(["Time","Core1", "Core2", "Core3","Core4","Core5","Core6","Core7","Core8"])

for x in range(5):
    import pdb;pdb.set_trace()
    import time
    cpu_usage=psutil.cpu_percent(interval=1, percpu=True)
    time = time.strftime('%X')
    cpu_usage.insert(0,time)
    csv_write(cpu_usage)
