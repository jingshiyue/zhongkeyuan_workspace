# import numpy as np
import matplotlib.pyplot as plt
import datetime,time

colors = {
        1: 'red',
        2: 'green',
        3: 'blue',
        4: 'brown',
        5: 'cyan',
        6: 'orange',
        7: 'pink',
        8: 'purple',
        9: 'royalblue',
        10: 'yellow',
        11: 'darkgray',
        12: 'gold',
        13: 'gray',
        14: 'navy',
        15: 'violet'}

def find_str(str,searchStr,offset):
        start = str.find(searchStr) + len(searchStr)
        content = str[start+1:start+offset]
        return content

def str2timestamp(time_str,format="%Y-%m-%d %H:%M:%S"):   #格式 ："%Y-%m-%d %H:%M:%S"
        timeArray = time.strptime(time_str, format)  # 先转换为时间数组
        timeStamp = int(time.mktime(timeArray))  #转换为时间戳 单位是秒
        return timeStamp

def timestamp2str(timestamp,format="%Y-%m-%d %H:%M:%S"):
        return time.strftime(format,time.localtime(timestamp))



if __name__ == '__main__':

    f = open(r"D:\workfile\zhongkeyuan_workspace\SDK_autoTest\cpu_memery_read\Monitor_CPU_RAM_20191009172907.txt", "r")
    cpu,ram,t = [],[],[]
    start_time = f.readline()[0:19]
    _start = str2timestamp(start_time)
    _xticks = []
    line = f.readline()
    while (line):
        if "Memory" in line:
            _memory = float((find_str(line, "Memory", 3)))
        if "CPU" in line:
            _cpu = float((find_str(line, "CPU", 5)))
        if "2019" in line:
            _t = '%.2f' % ((str2timestamp(line[0:19]) - _start) / 3600)
            _t = float(_t)
        cpu.append(_cpu)
        ram.append(_memory)
        t.append(_t)
        line = f.readline()
    offset = t[-1] / 10
    for i in range(11):
        _xticks.append(offset * i)

    plt.figure(dpi=128, figsize=(10, 7))
    plt.plot(t, cpu, label="CPU", color=colors[2], linestyle='-')
    plt.plot(t, ram, label="RAM", color=colors[10], linestyle='-')
    plt.xlabel("time(hour)")
    plt.ylabel("Occupancy rate")
    plt.title("Resource statistics")
    plt.legend(loc='upper left')
    plt.xticks(_xticks)
    plt.ylim(0, 100)
    plt.savefig("test.png")
    f.close()