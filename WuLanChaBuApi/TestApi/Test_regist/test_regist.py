# coding:utf-8
from WuLanChaBuApi.TestApi.new_method import *
from WuLanChaBuApi.TestApi.Test_regist.Regist import Regist
import pytest
import json
from WuLanChaBuApi.common.mysql_class import *
shujuku = DataBase("192.168.1.107", 3306, "root", "123456", "faceguard")


def test_delete_01():
    """验证删除不存在的人脸信息时服务器能给出正确的相应"""
    body = {"reqId": get_uuid(),
            "personCode": "684"}
    res = Regist().api_v1_face_delete(body)
    json_data = json.loads(res)
    assert json_data["status"] == 108


@pytest.mark.skip(reason="不测试")
def test_query_01():
    """对人脸信息查询"""
    body = {"reqId": get_uuid(),
            "name": "",
            "personCode": "",
            "pageNum": "1",
            "pageSize": "10",
            "isCount": "1",
            "faceLibId": "402881e96796dd4101679718c02a003f"}
    res = Regist().api_v1_face_query(body)
    # assert json.loads(res)["results"][0]["departmentName"] == '智能安全技术研究中心'


def test_detail():
    """人脸信息详情查询"""
    body = {"reqId": get_uuid(),
            "personId": "d382d52b0287447ea31b518e75cae78b"}
    Regist().api_v1_face_detail(body)


def test_update():
    """人脸信息更新接口"""
    body = {"reqId": get_uuid(),
            "num": "1",
            "registInfo": [{"name": "修改的姓名121111111111111111111111111111",
                            "sex": 1,
                            "birthdayDate": "00000000",
                            "nationality": "中国666",
                            "ethnic": "修改",
                            "personCode": "studentpersoncode4",
                            "codeType": "1",
                            "expiredTime": "111",
                            "cobDepartmentId": "4028806a674f79d50167585a58bf00ba",
                            "faceImg": to_base64(r"C:\chenkeyun\projectself\pythonproject\WuLanChaBuApi\common\picture\1.jpg")}]
    }
    Regist().api_v1_face_update(body)


# @pytest.mark.skip(reason="")
def test_binding_01():
    relations = []
    """修改人脸信息与人脸库的绑定接口"""
    yuanzu = shujuku.find_all("SELECT face_image.id FROM face_image;")
    for i in range(0, 1002):
        relations_one = {"personId": yuanzu[i][0],
                         "faceLibIds": "402881e967a6e9200167a7044c4a514f",
                         "optType": 2,
                         "fId": get_uuid()}
        relations.append(relations_one)
    relations = json.dumps(relations)
    body = {
        "reqId": get_uuid(),
        "relations": relations,
        "num": 1002
    }
    Regist().api_v1_face_lib_binding(body)

if __name__ == '__main__':
    pytest.main(["-q", "test_regist.py"])
