# coding:utf-8
from WuLanChaBuApi.TestApi.client_test.Client import *
import pytest
import os
import json
import time

current_path = os.path.realpath(__file__)
dirpath = os.path.dirname(current_path)
dirpath = os.path.dirname(dirpath)
dirpath = os.path.dirname(dirpath)
picpath = os.path.join(dirpath, "common\\picture")
featurepath = os.path.join(dirpath, "common\\features")


def test_client_regist():
    """客户端向服务器注册"""
    body = {"reqId": get_uuid(),
            "deviceCode": "test1",
            "areaCode": "T411",
                }
    Client().api_client_regist(body)


def test_push_regist():
    """客户端向服务器注册人脸信息"""
    _faceInfos = []
    for i in range(40, 60):
        faceInfosone = {"faceImageId": get_uuid(),
                         "optType": 0,
                         "name": "酉时三刻醉死鬼%d" % i,
                         "sex": 1,
                         "birthdayDate": "19920808",
                         "nationality": "地狱",
                         "ethnic": "汉族",
                         "personCode": "酉时三刻醉死鬼%d" % i,
                         "codeType": "0",
                         "expiredTime": "",
                         "cobDepartmentId": "402881e96796dd41016796f579690028",
                         "faceImg": to_base64(picpath+"\\"+"%d.jpg" % i),
                         "feature": get_features((picpath+"\\"+"%d.jpg" % i), mode="2K"),
                         "faceLibId": "402881e9679b7c6e01679b9afcc70002"}
        _faceInfos.append(faceInfosone)

    body = {"reqId": get_uuid(),
            "deviceCode": "Device3",
            "num": _faceInfos.__len__(),
            "faceInfos": _faceInfos
            }
    Client().api_client_push_syncdata(body)


def test_ask_syncdata():
    """客户端询问服务器是否有对应增量信息接口"""
    body1 = {"reqId": get_uuid(),
             "deviceCode":  "Device1",
             "faceLibIds": "4028806a675e63ba01675e8f6f620257"}   # 经过测试 和faceLibIds无关系
    Client().api_client_ask_syncdata(body1)


def test_pull_syncdata():
    """3.3.4客户端请求服务器增量人脸数据接口"""
    syncInfos = []
    i = random.randint(0, 100)
    for k in range(0, i):
        syncInfos_one = {"id": "4028806a676296ac0167629db607000b",
                         "faceLibraryId": "4028806a675e63ba01675e8f6f620257",
                         "faceImageId": "14645b46dc084b39a30107d267fe5b44"}
        syncInfos.append(syncInfos_one)

    body = {"reqId": get_uuid(),
            "deviceCode": "ClentTestOnce",
            "syncInfos": syncInfos,
            "num": i}
    res = json.loads(Client().api_v1_client_pull_syncdata(body))
    assert res["num"] == i


def test_confirm_syncdata_01():
    """3.3.5客户端确认服务器增量数据的接口  deviceCode为空的时候"""
    body = {"reqId": get_uuid(),
            "deviceCode": "",
            "syncInfos": "121"}       # 增量表3.6的id，多条数据以逗号分隔
    res = Client().api_v1_client_confirm_syncdata(body)
    assert json.loads(res)["msg"] == "bad params<deviceCode is empty> "


def test_confirm_syncdata_02():
    """3.3.5客户端确认服务器增量数据的接口  syncInfos为空的时候"""
    body = {"reqId": get_uuid(),
            "deviceCode": "111",
            "syncInfos": ""}       # 增量表3.6的id，多条数据以逗号分隔
    res = Client().api_v1_client_confirm_syncdata(body)
    assert json.loads(res)["msg"] == "bad params<syncinfos is empty> "


def test_confirm_syncdata_03():
    """3.3.5客户端确认服务器增量数据的接口 正确的值"""
    # 没有校验是哪个客户端
    body = {"reqId": get_uuid(),
            "deviceCode": "TestDemo",
            "syncInfos": "402881e9679b1aa101679b3ac2f80035,402881e9679b1aa101679b2efadb0009,402881e9679b1aa101679b2efa8d0008"}
    # 增量表3.6的id，多条数据以逗号分隔   # 对id不做校验是否已经被删除，只要没被删除就会被删除
    res = Client().api_v1_client_confirm_syncdata(body)


def test_pull_alldata():
    """3.3.6客户端请求服务器全部底库同步接口"""
    i = random.randint(1, 41)
    body = {"reqId": get_uuid(),
            "deviceCode": "test2",
            "faceLibId": "402881e9679c519c0167a05e2ffe4820",
            "pageNum": "1",
            "pageSize": 2}
    res = Client().api_v1_client_pull_alldata(body)
    try:
        assert json.loads(res)["num"] == 2
    except Exception as A:

        raise A


def test_delete_alldata():
    """3.3.7客户端请求清空对应的增量信息表"""
    start = time.clock()
    body = {"reqId": get_uuid(),
            "deviceCode": "TestDemo",
            "faceLibIds": "4028806a676296ac0167639afb0700a1"
    }
    res = Client().api_v1_client_delete_alldata(body)
    end = time.clock()
    print("服务器响应时间为:%ss" % (end-start))
    assert json.loads(res)["status"] == 0


if __name__ == '__main__':
    pytest.main(["-q", "test_client.py"])

