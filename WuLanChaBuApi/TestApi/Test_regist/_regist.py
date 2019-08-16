# coding:utf-8
import pytest
from WuLanChaBuApi.TestApi.new_method import *
import os
from WuLanChaBuApi.TestApi.Test_regist.Regist import Regist

# def test_01():
#     """能进行单个人脸进行注册"""
current_path = os.path.realpath(__file__)
dirpath = os.path.dirname(current_path)
dirpath = os.path.dirname(dirpath)
dirpath = os.path.dirname(dirpath)
picpath = os.path.join(dirpath, "common\\picture")   # 获得图片的路径
print(picpath)

if __name__ == '__main__':
    registInfos = []
    for i in range(40, 41):
        registInfo_1 = {
                        "name": "5QQstudent%s" % i,
                        "sex": 0,
                        "birthdayDate": "19951213",
                        "nationality": "中国",
                        "ethnic": "满族",
                        "personCode": "5rdgkkaefse12154",  # "studentpersoncode%d" % i
                        "codeType": "0",
                        "expiredTime": "20181213",
                        "cobDepartmentId": "q02881e96796dd41016796f579690028",
                        "faceImg": to_base64(picpath+"\\"+"%d.jpg" % i)
                        # "faceImg": to_base64("C:\\Users\\Original Dream\\Desktop\\UD{%TA)5R5VV@N~G`OR)_EY.jpg")
                        }
        registInfos.append(registInfo_1)

    body = {"reqId": get_uuid(),
            "num": registInfos.__len__(),
            "registInfo": registInfos}
    Regist().api_v1_face_regist(body)
