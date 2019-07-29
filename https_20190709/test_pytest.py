#!/usr/bin/python3
# Time : 2019/7/12 9:29 
# Author : zcl
import pytest
import random
#
# @pytest.mark.parametrize("x,y", [(1,2),(2,3),(3,4)])
def test_foo(x,y):
    print("测试数据组合：x->%s, y->%s" % (x,y))

def test_foo1(*d):
    print(d)


file = [1,2,3,4]
f = tuple(file)
print(f)
f1 = (str(f))
print(type(f1))