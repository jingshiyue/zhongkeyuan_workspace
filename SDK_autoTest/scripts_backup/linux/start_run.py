#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import subprocess
# import psutil
import os,datetime,time
import threading
import logging
import configparser
import sys
import traceback
PATH = os.path.abspath(__file__)[0:os.path.abspath(__file__).rfind("/")]
os.chdir(PATH)
sys.path.append(PATH + "\\myUtils")   
print(os.getcwd())

def start_threading(command):
    os.system(command)


if __name__=="__main__":   
    t = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    try:
        if  os.path.exists("./result.log"):
            os.system("rm -rf result.log")
        if  os.path.exists("./testbed.ini"):
            os.system("rm -rf testbed.ini")
        
        time.sleep(3)
        config = configparser.ConfigParser()
        config.read(r"./testbed.ini")
        
        config.add_section("testbed")
        config.set("testbed","env","Ubuntu 16.04.6 LTS")
        config.set("testbed","file","./result/tmp/LINUX_%s/SdkTestbed.log" %t)
        config.set("testbed","resultPath","./result/tmp/LINUX_%s" %t)
        with open("./testbed.ini", 'w') as config_file:
            config.write(config_file)
        os.makedirs(config.get("testbed","resultPath")) 
        env = config.get("testbed","env")
        log_path = config.get("testbed","file")
        
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(message)s',
                            filename = log_path,
                            filemode='a')
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        console.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(console)    
        
        t1 = threading.Thread(target = start_threading,args=("python3 ./myUtils/query_cpu_ram.py",))
        t1.setDaemon(True)
        t1.start()
        
        s=subprocess.Popen(r"python3 ./test.py",shell=True,bufsize=0,stdout=subprocess.PIPE,universal_newlines=True)   
        try:
            while True:
                nextline=s.stdout.readline()
                logging.debug(nextline.strip())
                if nextline=="" and scan.poll()!=None:
                    logging.debug("test cases complate ...")
                    break
        except:
            logging.debug("test cases complate ...")  
            
        os.system(r"python3 ./myUtils/analyse_sdk_result.py")    
        os.system(r"python3 ./myUtils/readCaseExcel_outputHtml.py")  
        os.system(r"python3 ./myUtils/sendmail.py")
        os.system("ps -ef|grep python|grep -v grep|cut -c 9-15|xargs kill -9")
    except:
        f = open(r"./result.log",'a')
        traceback.print_exc(file = f)
        f.flush()
        f.close()
        os.system("ps -ef|grep python|grep -v grep|cut -c 9-15|xargs kill -9")
