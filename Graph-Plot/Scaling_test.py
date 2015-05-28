#sudo apt-get install python-gnuplot
import os
import time

def find_between(se,first,last):
    se="".join(line.rstrip() for line in se)
    try:
        start = se.index( first ) + len( first )
        end = se.index( last, start )
        return se[start:end]
    except ValueError:
        return ""

def execute_command(cmd):
    command = " ".join(cmd)
    p = os.popen(command,'r')
    line = p.readlines()
    return line

def draw_graph(conn,com_req,response):
    #!/usr/bin/env python
    import numpy as np
    import Gnuplot
    from numpy import array
    #Create some data
    x = np.array(conn)
    y1 = np.array(com_req)
    y2 = np.array(response)
    #Instantiate Gnuplot object
    g = Gnuplot.Gnuplot(persist=1)
    #Create the Gnuplot data
    req_per_sec = Gnuplot.Data(x,y1,with_='lp',title='req_per_sec')
    response_time = Gnuplot.Data(x,y2,with_='lp',title='response_time')
    #Formatting options
    g('set grid')
    g('set key left')
    #Plot

    g.plot(req_per_sec,response_time)
    g.hardcopy('gp_test.ps', enhanced=1, color=1)
    g.reset()

req_sec=5000
max_conn= 100
adc_IP = "30.0.1.2"
rps=[]
conn=[]
com_req=[]
response=[]
for x in range(10,max_conn,10):
    cmd = ["sudo  ab -n %s -c %s -t 1   \"http://%s/512.txt\""%(req_sec,x,adc_IP)]
    #time.sleep(1)
    output = execute_command(cmd)
    com_req.append(float((find_between( output, "Complete requests:", "Failed requests:" )).split()[0]))
    conn.append(x)
    rps.append(req_sec)
    response.append(float((find_between( output, "[ms] (mean)Time per request:", "[ms]" )).split()[0]))

print "INPUT request per second is -- %s"%rps
print "INPUT concurrent connection is -- %s"%conn
print "Completed requests is -- %s"%com_req
print "Time per sec is -- %s"%response
draw_graph(conn,com_req,response)