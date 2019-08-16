# coding:utf-8
from WuLanChaBuApi.TestApi.new_method import *


class DataDict(object):
    """数据字典值信息"""
    def __init__(self):
        self.hostaddress = "http://192.168.1.105:9009/face-door-guard/"    # face-door-guard/
        self.allprocessdictquery = self.hostaddress + "api/v1/system/dictory/query"
        self.allprocessdictupdate = self.hostaddress + "api/v1/system/dictory/update"
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def get_header(self,newsign):
        timestamp = get_time_stamp()
        sign = to_md5_str(newsign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    def api_system_dictory_query(self, body, sign_only="/api/v1/system/dictory/query"):
        header = self.get_header(sign_only)
        res = requests.post(url=self.allprocessdictquery,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_system_dictory_update(self, body, sign_only="/api/v1/system/dictory/update"):
        header = self.get_header(sign_only)
        res = requests.post(url=self.allprocessdictupdate,
                            headers=header,
                            json=body,
                            verify=False)
        print(res.text)
        return res.text

if __name__ == '__main__':
    dictdata = DataDict()
    body1 = {"reqId": get_uuid()}
    dictdata.api_system_dictory_query(body1)
    dictdata.api_system_dictory_update(body1)



