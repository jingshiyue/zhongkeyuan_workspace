# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_pre_security_passnum(body):
    """
    调用2.4.8.3预安检区域通过人数接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/analysis/pre-security/passnum"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/pre-security/passnum" + timestamp + apiKey
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
    body = {
        "reqId": "32位UUID",
        "areaCode": "T1YA1",  # 通道编号(区域表里面的编号)
        "startTime": "20181113000000",
        "endTime": "20181211000000"
        }
    api_v1_analysis_pre_security_passnum(body)