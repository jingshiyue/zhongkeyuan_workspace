import subprocess
import psutil
import os,datetime,time
import threading
import logging
import configparser
import sys
import traceback
os.chdir(os.path.dirname(__file__)) 
sys.path.append(os.path.dirname(__file__) + "\\myUtils")   

    
if __name__=="__main__":   
    try:
        if  os.path.exists("./result.log"):
            os.system("del /s /q result.log")
        #step one
        os.system(r".\run.bat")   
        
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
        
        #step two
        s=subprocess.Popen(r".\test.bat",shell=True,bufsize=0,stdout=subprocess.PIPE,universal_newlines=True)   
        try:
            while True:
                nextline=s.stdout.readline()
                logging.debug(nextline.strip())
                if nextline=="" and scan.poll()!=None:
                    logging.debug("test cases complate ...")
                    break
        except:
            logging.debug("test cases complate ...")  
            
        #step three
        os.system(r".\myUtils\analyse_sdk_result.py")    
        #step four
        os.system(r".\myUtils\readCaseExcel_outputHtml.py")  
        #step five
        os.system(r".\myUtils\sendmail.py")   
    except:
        f = open(r"./result.log",'a')
        traceback.print_exc(file = f)
        f.flush()
        f.close()
        os.system("TASKKILL /F /IM python.exe /T") 
        logging.debug("TASKKILL /F /IM python.exe")












