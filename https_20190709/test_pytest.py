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


str = "验证 reqId="" 时，服务器能正确响应"
l = str.split(" ")
p1 = (l[1].split("=")[0])
print(p1)
p2 = (l[1].split("=")[1])
print(p2)
assert p2==""
