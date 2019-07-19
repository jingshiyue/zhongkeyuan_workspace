# coding:utf-8
# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_passenger_security(body):
    """
    调用旅客个人安检信息查询接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/analysis/passenger/security"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/passenger/security" + timestamp + apiKey
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
        "name": "陈克云",
        "num": "500238199312134390",            # 身份证
        "count": "3"  # 最近几次 不给默认3次
        }
    api_v1_analysis_passenger_security(body)