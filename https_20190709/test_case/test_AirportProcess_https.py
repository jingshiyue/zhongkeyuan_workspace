#!/usr/bin/python3
# Time : 2019/7/23 8:57 
# Author : zcl
# from https_20190709.API_https.BlackList import *
import pytest
from https_20190709.common.common_method import *
from https_20190709.common.params_init_z import *
from https_20190709.API_https.AirportProcess import *
from https_20190709.common.Log_z import mylog
logger = mylog.get_log().get_logger()



# host = "https://192.168.5.15:4433/security-server"
# certificate_file = "D:/workfile/workspace/https_20190709/API_https/cacert.crt"

test_param = stru_params_tuple("my_interface_test.yml","test_api_face_security_face_check")
print(test_param)

# class Test_AirportProcess():
#
#     def setup_class(cls):
#         cls.ap = AirportProcess()
#
#     @pytest.mark.parametrize(str(tuple(get_params_list("my_interface_test.yml","test_api_face_security_face_check"))), test_param)
#     def test_api_face_security_face_check(self,tuple(get_params_list("my_interface_test.yml","test_api_face_security_face_check"))):
#         res = cls.ap.api_face_security_face_check(tuple(get_params_list("my_interface_test.yml","test_api_face_security_face_check"))
#         # logger.debug(res.text)
#
# if __name__=="__main__":
#     pytest.main(["-s","test_AirportProcess_https.py"])