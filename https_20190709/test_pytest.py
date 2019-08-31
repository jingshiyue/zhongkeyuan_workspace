#!/usr/bin/python3
# Time : 2019/7/12 9:29 
# Author : zcl
import pytest
import random
import pytest
params = {1:"",2:2}

log_param = ""
for key,value in params.items():
    if params[key] == "":
        log_param = key
        print("当前参数:%s 为空" %log_param)




# if __name__=="__main__":
#     pytest.main(["-s","test_pytest.py"])