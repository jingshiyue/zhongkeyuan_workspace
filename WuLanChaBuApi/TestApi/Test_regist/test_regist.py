# coding:utf-8
from WuLanChaBuApi.TestApi.new_method import *
from WuLanChaBuApi.TestApi.Test_regist.Regist import Regist
import pytest
import json
from WuLanChaBuApi.common.mysql_class import *
shujuku = DataBase("192.168.5.15", 3306, "root", "123456", "faceguard")


@pytest.mark.skip(reason="")
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
    assert json.loads(res)["results"][0]["departmentName"] == '智能安全技术研究中心'


@pytest.mark.skip(reason="")
def test_detail():
    """人脸信息详情查询"""
    body = {"reqId": get_uuid(),
            "personId": "d382d52b0287447ea31b518e75cae78b"}
    Regist().api_v1_face_detail(body)


# @pytest.mark.skip(reason="")
def test_update():
    """人脸信息更新接口"""
    body = {"reqId": get_uuid(),
            "num": "1",
            "registInfo": [{"name": "正常考勤101",
                            "sex": 1,
                            "birthdayDate": "19900101",
                            "nationality": "中国",
                            "ethnic": "汉",
                            "personCode": "500382199001017022",
                            "codeType": "1",
                            "expiredTime": "",
                            "cobDepartmentId": "4028858f6ccd13c0016ccd1a88a3000b",
                            "faceImg": to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\100.jpg")}]
    }
    Regist().api_v1_face_update(body)
    print("mte")


@pytest.mark.skip(reason="人脸信息与人脸库的绑定接口")
def test_binding_01():
    relations = []
    """修改人脸信息与人脸库的绑定接口"""
    # yuanzu = shujuku.find_all("SELECT face_image.id FROM face_image;")
    # for i in range(0, 1002):
    #     relations_one = {"personId": yuanzu[i][0],
    #                      "faceLibIds": "402881e967a6e9200167a7044c4a514f",
    #                      "optType": 2,
    #                      "fId": get_uuid()}
    #     relations.append(relations_one)
    # relations = json.dumps(relations)

    relations_one = {"personId": "e1ebf165008a4aa385d2277618817d8d",
                     "faceLibIds": "4028858f6cd61b18016cd65d511c010b",
                     "optType":0,  #0-新增，1-修改。2-删除
                     "fId": get_uuid()}
    relations.append(relations_one)
    relations = json.dumps(relations)

    body = {
        "reqId": get_uuid(),
        "relations": relations,
        "num": 1
    }
    Regist().api_v1_face_lib_binding(body)


@pytest.mark.skip(reason="注册人脸信息,存在人脸信息表里")
def test_face_regist(): #注册人脸信息
    pic_path = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\100.jpg"
    _registInfo = [
        { "name":"正常考勤101",
         "sex":1,
         "personCode":"500382199001017022",
         "cobDepartmentId":"AA00101",    #String    32位部门ID，对应3.3的部门表的ID
         "faceImg":to_base64(pic_path),
          "birthdayDate":"19900101",
          "nationality":"中国",
          "ethnic":"汉",
          "codeType":1
       }]

    body = {
         "reqId":get_uuid(),
         "num":1,
         "registInfo":_registInfo
    }

    res = Regist().api_v1_face_regist(body)
    print(res.text)


if __name__ == '__main__':
    pytest.main(["-s", "test_regist.py"])
