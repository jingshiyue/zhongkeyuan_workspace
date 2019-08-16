#!/usr/bin/python3
# Time : 2019/7/12 9:29 
# Author : zcl
import pytest
import random
import pytest
from BaiTaAirport2_month.common.mysql_class import *
# def f(p1="",p2=""):
#     print(p2)
#     print(p1)
#     return 1
#
#
# @pytest.mark.parametrize('p1,p2',[({"p11":5},{"p22":4}),])
# def test_f(p1,p2):
#     a = p1["p11"]
#     b = p2["p22"]
#     f(a,b)


@pytest.fixture()
def first():
    print("获取用户名")
    a = "yoyo"
    return a

# @pytest.fixture()
# def sencond(first):
#     '''psw调用user fixture'''
#     a = first
#     b = "123456"
#     return (a, b)
#
# def test_1(sencond):
#     '''用例传fixture'''
#     print("测试账号：%s, 密码：%s" % (sencond[0], sencond[1]))
#
#     assert sencond[0] == "yoyo"
#
# if __name__ == "__main__":
#     pytest.main(["-s", "test_pytest.py"])
import requests
certificate = "D:\workfile\zhongkeyuan_workspace\https_20190709\API_https\cacert.crt"
raw = open(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\0.jpg","rb")
raw = raw.read()

url = "https://192.168.5.15:9090/data-platform-server/api/v1/resource/group1/M00/A5/BF/wKgFDl1SYcCAUZ-WAAAyr2moAmg757.jpg"
res = requests.get(url=url,verify=certificate)
print(len(res.content))
print((res.content))