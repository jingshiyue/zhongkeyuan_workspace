# coding:utf-8
# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_face_pre_security_query(body):
    """
    调用预安检旅客数据查询接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/face/pre-security/query"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/face/pre-security/query" + timestamp + apiKey
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
    print(res.elapsed.total_seconds())
    return res.text


if __name__ == '__main__':
    start = time.clock()
    body = {
        "reqId": get_uuid(),
        # "name": "",
        # "englishName": "",
        # "cardType": "",
        # "idCard": "",
        # "sex": "",
        # "areaCode": "",
        # "matchResult": "",
        "startTime": "20180701091232",
        "endTime": "20181201091232",
        "page": "10000",  # int
        "pageSize": "50",
        "isCount": "1"

        }
    api_v1_face_pre_security_query(body)
    end = time.clock()
    print(end-start)
