# coding:utf-8
import time

import requests

if __name__ == '__main__':
    # shujuku = DataBase("192.168.1.107", 3306, "root", "123456", "faceguard")
    # a = shujuku.find_all("SELECT face_image.id FROM face_image;")
    # print(a[0])
    # print(a[0][0])
    # print(type(a[0][0]))
    time1 = time.clock()
    res = requests.get(url="http://192.168.1.105:9009/face-door-guard/api/v1/resource/group1/"
                           "M00/00/8B/oYYBAFwROW6AGgQ2AACQVt3NFRw837.jpg")
    time2 = time.clock()
    print(time2-time1)
    print(res.content.__len__())