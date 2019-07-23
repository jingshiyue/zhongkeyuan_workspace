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

class Test_AirportProcess():

    def setup_class(self):
        self.ap = AirportProcess()

    @pytest.mark.parametrize("param", test_param)
    def test_api_face_security_face_check(self,param):
        logger.debug(param)

        res = self.ap.api_face_security_face_check(
                                param
                                # reqId=test_param["reqId"],
                                # gateNo=test_param["gateNo"],
                                # deviceId=test_param["deviceId"],
                                # cardType=test_param["cardType"],
                                # idCard=test_param["idCard"],
                                # nameZh=test_param["nameZh"],
                                # nameEn=test_param["nameEn"],
                                # age=test_param["age"],
                                # sex=test_param["sex"],
                                # birthDate=test_param["birthDate"],
                                # address=test_param["address"],
                                # certificateValidity=test_param["certificateValidity"],
                                # nationality=test_param["nationality"],
                                # ethnic=test_param["ethnic"],
                                # contactWay=test_param["contactWay"],
                                # scenePhoto=test_param["scenePhoto"],
                                # sceneFeature=test_param["sceneFeature"],
                                # cardPhoto=test_param["cardPhoto"],
                                # cardFeature=test_param["cardFeature"],
                                # largePhoto=test_param["largePhoto"]
                            )

if __name__=="__main__":
    pytest.main(["-s","test_AirportProcess_https.py"])