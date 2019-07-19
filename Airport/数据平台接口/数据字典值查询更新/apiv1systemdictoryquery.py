# coding:utf-8
import requests
from Airport.new_method import *


class ApiSystemDictory(object):
    """
    全流程字典值查询和更新
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/system/dictory/query"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/dictory/query" + timestamp + apiKey
    sign2 = to_md5_str(sign1)
    header = {"apiId": apiId,
              "sign": sign2,
              "timestamp": timestamp,
              "Content-Type": "application/json; charset=utf-8"}

    def __init__(self):
        pass

    @classmethod
    def api_v1_system_dictory_query(cls, body):
        res = requests.post(url=cls.url,
                            headers=cls.header,
                            json=body,
                            verify=False)
        print(res.text)
        return res.text

    @classmethod
    def api_v1_system_dictory_update(cls, body):
        res = requests.post(url=cls.url,
                            headers=cls.header,
                            json=body,
                            verify=False)

        print(res.text)
        return res.text

if __name__ == '__main__':
        body1 = {
            "reqId": get_uuid()
        }
        ApiSystemDictory.api_v1_system_dictory_query(body1)
