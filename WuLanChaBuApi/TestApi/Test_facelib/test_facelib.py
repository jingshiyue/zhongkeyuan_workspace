# coding:utf-8
import pytest
from WuLanChaBuApi.TestApi.new_method import *
import json
from WuLanChaBuApi.TestApi.Test_facelib.FaceLib import FaceLib
from WuLanChaBuApi.common.mysql_class import DataBase


def test_create_01(delete_facelib):
    """验证能成功创建人脸底库"""
    body = {"reqId": get_uuid(),
            "libraryName": "室内办公人员",
            "libraryCode": "AA001",
            "libraryType": 1,
            "remark": "在室内办公人员在这个底库"}
    res = FaceLib().api_v1_facelib_create(body)
    json_data = json.loads(res)
    assert json_data["status"] == 0


@pytest.mark.skip(reason="不做测试")
def test_create_02():
    """新增创建人脸底库作为测试，其中name和code都不能重复"""
    body = {"reqId": get_uuid(),
            "libraryName": "生命一班11",
            "libraryCode": "lifeclass11",
            "libraryType": 2000000,
            "remark": "建立生命一班学生"}

    res = FaceLib().api_v1_facelib_create(body)
    json_data = json.loads(res)
    assert json_data["status"] == 0


def test_update_01():
    """底库更新"""
    # __test_create_02()
    body1 = {"reqId": get_uuid(),
             "id": "402881e96796dd410167971d2ad50044",
             "libraryName": "更新0000",
             "libraryCode": "code00",
             "libraryType": "1",
             "remark": ""}
    res = FaceLib().api_v1_facelib_update(body1)
    json_data = json.loads(res)
    assert json_data["status"] == 0


def test_delete_01():
    """底库删除"""
    # 先新增底库
    body = {"reqId": get_uuid(),
            "libraryName": "A0001",
            "libraryCode": "newzeng",
            "libraryType": 1,
            "remark": ""}

    FaceLib().api_v1_facelib_create(body)
    shuju = DataBase("192.168.1.107", 3306, "root", "123456", "faceguard")
    shuju.open_data_base()
    sql1 = "select * FROM face_library WHERE library_code='newzeng';"
    data = shuju.find_all(sql1)
    print("新增后的数据为:")
    print(data)
    time.sleep(1)
    key_id = data[0][0]
    body1 = {"reqId": get_uuid(),
             "ids": key_id}
    res = FaceLib().api_v1_facelib_delete(body1)
    json_data = json.loads(res)
    assert json_data["status"] == 0


def test_delete_02():
    """底库删除test多个"""
    body1 = {"reqId": get_uuid(),
             "ids": "402881e96796dd41016797289ead0048,402881e96796dd410167972103d00047"}
    FaceLib().api_v1_facelib_delete(body1)


def test_query_01():
    """对底库进行查询"""
    body = {"reqId": get_uuid(),
            "libraryName": "生命",
            "isCount": 0,
            "pageNum": 1,
            "pageSize": 0}
    res = FaceLib().api_v1_facelib_query(body)


if __name__ == '__main__':
    pytest.main(["-q", "test_facelib.py"])