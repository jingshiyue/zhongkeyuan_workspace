import psutil
import os,datetime,time
import threading
import logging
import configparser
config = configparser.ConfigParser()
config.read(r"./testbed.ini")
env = config.get("testbed","env")
resultPath = config.get("testbed","resultPath")
log_path = resultPath + "/Monitor.log"

config.set("testbed","monitorlog",log_path)
with open("./testbed.ini", 'w') as config_file:
    config.write(config_file)


logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    filename = log_path,
    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
console.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console)


def getMemCpu():
    data = psutil.virtual_memory()
    # total = data.total #总内存,单位为byte
    # free = data.available #可以内存
    memory = "Memory:%d"%(int(round(data.percent)))+"%"+" "
    cpu = "CPU:%0.2f"%psutil.cpu_percent(interval=1)+"%"
    logging.info(memory+cpu)
    timer = threading.Timer(60*2,getMemCpu)
    timer.start()

 
if __name__=="__main__":
    query_timer = threading.Timer(0,getMemCpu)
    query_timer.start()