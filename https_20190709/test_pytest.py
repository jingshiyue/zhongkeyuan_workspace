#!/usr/bin/python3
# Time : 2019/7/12 9:29 
# Author : zcl
import pytest
import random
import pytest
def f(p1="",p2=""):
    print(p2)
    print(p1)
    return 1


@pytest.mark.parametrize('p1,p2',[({"p11":5},{"p22":4}),])
def test_f(p1,p2):
    a = p1["p11"]
    b = p2["p22"]
    f(a,b)


dic = {"p1":1,"p2":2,"p3":3}
tu = (1,2,3)

if __name__=="__main__":
    pytest.main(["-s","test_pytest.py"])