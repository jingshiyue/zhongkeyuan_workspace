# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_passenger_sexrate(body):
    """
    调用2.4.7.1旅客性别人数分布
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/analysis/passenger/sexrate"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/passenger/sexrate" + timestamp + apiKey
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
    start = time.clock()
    body = {
        "reqId": get_uuid(),
        "startTime": "2018092208000000",
        "endTime": "2018122308000000"
        }
    api_v1_analysis_passenger_sexrate(body)
    end = time.clock()
    print(end-start)