__author__ = 'Aayush Bhardwaj'

#http://pythonhosted.org/jenkinsapi/api.html
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
import re
import sys, getopt , json

myopts, args = getopt.getopt(sys.argv[1:],"j:b:")
for o, a in myopts:
    if o == '-j':
        job=a
    elif o == '-b':
        build_nos=a

def create_file(con):
    with open("Output.txt", "w") as text_file:
        text_file.write(con)

def extract_info():
    pass

def find_between(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def count_occurences(s,sub):
    count = s.count(sub)
    return count

def show_build_info():
    info={}
    with open("Output.txt") as myfile:
        data="".join(line.rstrip() for line in myfile)
    info["author"]=(find_between( data, "Started by user", "[EnvInject]" )).split()
    info["avniapps"]=(find_between( data, "avniapps", "[run" )).split().pop()
    info["avninode-production"]=(find_between( data, "avninode-production", "Copied" )).split().pop()
    info["hascheme"]=(find_between( data, "pytestparams: --hascheme", "Cloning" )).split().pop()
    info["testtype"]=(find_between( data, "--testtype ", " " )).split().pop()
    info["Controller_launch_time"]=(find_between( data, "Controller launched successfully in ", " " )).split().pop()
    info["TOTAL"]=(find_between( data, "[INFO]: A total of", "tests" )).split().pop()
    info['PASSED']=count_occurences(data,"Final Result: PASSED")
    info['FAILED']=count_occurences(data,"Final Result: FAILED")
    info['result_url']=build.get_result_url()
    info['result']=build.is_good()
    return info

j = Jenkins('http://65.49.10.67:8080','avniayush','avniayush')
#import pdb;pdb.set_trace()
#build = j['run-tests'].get_last_good_build()
build = j[job].get_build(int(build_nos))
#selective_build.is_running()
if not build.is_running():
    Console = build.get_console()
    create_file(Console)
    info = show_build_info()
    general_info = json.dumps(info)
    print general_info
else:
    print("The build is still running.")