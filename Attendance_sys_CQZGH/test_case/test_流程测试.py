#!/usr/bin/python3
# Time : 2019/8/22 13:45 
# Author : zcl
import pytest
from WuLanChaBuApi.TestApi.Test_facelib.FaceLib import FaceLib
from Attendance_sys_CQZGH.utils.common_method import *
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()


def test_Client_regist_process():
    body = [
        { "reqId": get_uuid(),
          "libraryName": "总工会领导",
          "libraryCode": "AA001",
          "libraryType": 1,
          "remark": "总工会领导"},

        {"reqId": get_uuid(),
         "libraryName": "办公室",
         "libraryCode": "AA002",
         "libraryType": 1,
         "remark": "办公室"},
    ]
    for i in range(10):
        tmp_dic = {
            "reqId": get_uuid(),
            "libraryName": "部门%d" %i,
            "libraryCode": "AA0%d" %i,
            "libraryType": 1,
            "remark": "部门%d" %i
        }
        body.append(tmp_dic)
    logger.info(body)
    # FaceLib().api_v1_facelib_create()


if __name__ == '__main__':
    pytest.main(["-q", "test_流程测试.py"])