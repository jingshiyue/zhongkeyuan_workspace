# coding:utf-8
# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_passenger_data(body):
    """
    调用旅客个人数据查询接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/analysis/passenger/data"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/passenger/data" + timestamp + apiKey
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
        "reqId": "1",
        "name": "",
        "num": "142724198605103941",            # 身份证
        "startTime": "20180701091232",
        "endTime": "20181201091232",
        }
    api_v1_analysis_passenger_data(body)