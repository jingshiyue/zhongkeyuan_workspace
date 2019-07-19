# coding:utf-8
import requests
from Airport.new_method import *
import json


def api_v1_face_pre_security_check(body):
    """
    预安检口1：1人脸验证
    :return:
    """
    url = "http://192.168.0.234:9090/presecurity-server/api/v1/face/pre-security/check"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/face/pre-security/check" + timestamp + apiKey
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
    with open(r"E:\test1000标准\id1000features\1.jpg\0.txt", "r") as fp:
        data1 = fp.read().rstrip()
        data2 = str(data1)
    feature_id =data2
    with open(r"E:\test1000标准\live1000features\1.jpg\0.txt", "r") as fp1:
        data3 = fp1.read().rstrip()
        data4 = str(data3)
    feature_live = data4
    m1 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.JPG")
    m2 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.JPG")

    body_data = {"reqId": get_uuid(),
                 "gateNo": "T1YA1",
                 "deviceId": "T1YA001",
                 "cardType": 0,     # 证件类型 int
                 "idCard": "500238199312134390",
                 "nameZh": "陈克云",
                 "nameEn": "CHENKEYUN",
                 "age": 25,  # int
                 "sex": 1,  # int
                 "birthDate": "19931213",
                 "address": "重庆市巫溪县朝阳镇",
                 "certificateValidity": "0-20191206",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": "中国",
                 "ethnic": "汉族",
                 "contactWay": "18680946659",
                 "scenePhoto": m2,
                 "sceneFeature": feature_live,
                 "cardPhoto": m1,
                 "cardFeature": feature_id,
                 "flightNo": "flight1",
                 "flightDay": "12",
                 "QTCode": "abcde",
                 "seatId": "3B",
                 "startPort": "1",
                 "boardingNumber": "777",
                 "fId": get_uuid()}
    try:
        data_2 = api_v1_face_pre_security_check(body_data)
        dict_data = json.loads(data_2)
        assert dict_data["result"] == 0
    except Exception as A1:
        with open("renlianyanzheng.txt","a+") as z1:
            z1.write("time:%s appear error---%s" % (get_time_mmss(), A1)+"\n")



