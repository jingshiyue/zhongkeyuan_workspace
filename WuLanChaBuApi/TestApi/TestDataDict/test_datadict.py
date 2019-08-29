# coding:utf-8
import pytest
import json
from WuLanChaBuApi.TestApi.TestDataDict.DataDict import *
DataDict_new = DataDict()


def test_01():
    """测试能正确查询出字典值数据"""
    body = {"reqId": get_uuid()}
    res = DataDict_new.api_system_dictory_query(body)
    json_data = json.loads(res)
    print(json_data)
    assert json_data["status"] == 0


# def test_02():
#     """验证uuid为空值是服务器能正确相应"""
#     body = {"reqId": ""}
#     res = DataDict_new.api_system_dictory_query(body)
#     json_data = json.loads(res)
#     assert json_data["status"] == 400
#
#
# def test_03():
#     """验证reqId为33位时服务器能正确相应,不对长度进行校验"""
#     body = {"reqId": get_uuid()+"11212121212"}
#     res = DataDict_new.api_system_dictory_query(body)
#     json_data = json.loads(res)
#     assert json_data["status"] == 0
#
#
# def test_04():
#     """验证数据库字典值变化后能成功更新"""
#     body = {"reqId": get_uuid()}
#     res = DataDict_new.api_system_dictory_update(body)
#     json_data = json.loads(res)
#     assert json_data["status"] ==0
#
#
# def test_05(add_dict_delete):
#     """测试能正确查询出字典值数据"""
#     print("Test_05")
#     body = {"reqId": get_uuid()}
#     res = DataDict_new.api_system_dictory_query(body)
#     json_data = json.loads(res)
#     assert json_data["result"]["4"]["1"] == 'android'

if __name__ == '__main__':
    pytest.main(["-q", " test_datadict.py"])
