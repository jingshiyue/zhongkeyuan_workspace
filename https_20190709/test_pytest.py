#!/usr/bin/python3
# Time : 2019/7/12 9:29 
# Author : zcl

import pytest
# from selenium import webdriver
# import time

class test1():
    def __init__(self):
        print("init")
    # def __new__(cls, *args, **kwargs):
    #     print("new")
    #     return super().__new__(cls)
    def print1(self):
        print("test1_print")
# isinstance(s, myclass)

class test2(test1):
    def __init__(self):
        print(self)
        test1.__init__(self)

test_b = test2()
# print(type(test_a))
# test1.__init__()
print("ok")