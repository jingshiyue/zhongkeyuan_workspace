# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_export_data(body):
    """
    调用2.4.10.1查询数据导出接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-paltform_server/api/v1/analysis/export/data"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/export/data" + timestamp + apiKey
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
        "serialNum": "d0f7072d4bad48a299f06c714f55ddfe",
        "exportName": "preSec",
        "startTime": "20181014134256",
        "endTime": "20181113134256"
        }
    api_v1_analysis_export_data(body)