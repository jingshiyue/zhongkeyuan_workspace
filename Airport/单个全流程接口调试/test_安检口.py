# coding:utf-8
import requests
from Airport.new_method import *
import json


def api_v1_face_security_check(body):
    """
    2.3.5安检口1;1人脸验证
    :param body:发送安检1：1比对请求到服务器的body
    :return:
    """
    url = "http://192.168.0.234:9090/security-server/api/v1/face/security/check"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/face/security/check" + timestamp + apiKey
    sign2 = to_md5_str(sign1)
    header = {"apiId": apiId,
              "sign": sign2,
              "timestamp": timestamp,
              "Content-Type": "application/json; charset=utf-8"}
    res = requests.post(url=url,
                        headers=header,
                        json=body,
                        verify=False)
    print(res.text)
    return res.text


if __name__ == '__main__':
    with open(r"E:\test1000标准\id1000features\3.jpg\0.txt", "r") as fp:
        data1 = fp.read().rstrip()
        data2 = str(data1)
    feature_id =data2
    with open(r"E:\test1000标准\live1000features\3.jpg\0.txt", "r") as fp1:
        data3 = fp1.read().rstrip()
        data4 = str(data3)
    feature_live =data4
    m1 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.JPG")
    m2 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.JPG")
    body_data = {"reqId": get_uuid(),
                 "gateNo": "T1AJ1",
                 "deviceId": "T1AJ001",
                 "cardType": 0,  # 证件类型 int
                 "idCard": "500238199312134391",
                 "nameZh": "陈克云1",
                 "nameEn": "CHENKEYUN1",
                 "age": 25,  # int
                 "sex": 1,  # int
                 "birthDate": "19931213",
                 "address": "重庆市巫溪县朝阳镇朝阳村",
                 "certificateValidity": "0-20191006",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": "中国",
                 "ethnic": "汉族",
                 "contactWay": "13815138378",
                 "scenePhoto": m2,
                 "sceneFeature": feature_live,
                 "cardPhoto": m1,
                 "cardFeature": feature_id}
    try:
        data_3 = api_v1_face_security_check(body_data)
        dict_data3 = json.loads(data_3)
        assert dict_data3["result"] == 0
    except Exception as A3:
        with open("anjiankou.txt", "a+") as z3:
            z3.write("time:%s appear error---%s" % (get_time_mmss(), A3)+"\n")