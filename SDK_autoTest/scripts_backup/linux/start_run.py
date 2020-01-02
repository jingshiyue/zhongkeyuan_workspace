import subprocess
import psutil
import os,datetime,time
import threading
import logging
import configparser
os.chdir(os.path.dirname(__file__)) 
    
if __name__=="__main__":   
    subprocess.Popen(r".\run.bat")
    time.sleep(3)
    config = configparser.ConfigParser()
    config.read(r"./testbed.ini")
    env = config.get("testbed","env")
    resultPath = config.get("testbed","resultPath")
    log_path = resultPath + "/SdkTestbed.log"   

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
    
    
    s=subprocess.Popen(r".\test.bat",shell=True,bufsize=0,stdout=subprocess.PIPE,universal_newlines=True)
    while True:
        nextline=s.stdout.readline()
        logging.debug(nextline.strip())
        if nextline=="" and scan.poll()!=None:
            break
    try:
        os.system("TASKKILL /F /IM python.exe /T") 
    except:
        logging.debug("TASKKILL /F /IM python.exe /T")
    
    # while s.poll() is None:
        # line = s.stdout.readline()
        # line = line.strip()
        # if line:
            # logging.debug(line.strip())
    # if s.returncode == 0:
        # print('Subprogram success')
    # else:
        # print('Subprogram failed')
    # try:
        # os.system("TASKKILL /F /IM python.exe /T") 
    # except:
        # logging.debug("TASKKILL /F /IM python.exe /T")














