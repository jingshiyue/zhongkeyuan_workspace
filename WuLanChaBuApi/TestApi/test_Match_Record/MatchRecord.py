# coding:utf-8
import requests
from WuLanChaBuApi.TestApi.new_method import *


class MatchRecord(object):
    def __init__(self,hostaddress="http://192.168.5.15:10019/"):
        """刷脸记录同步接口"""
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.hostaddress = hostaddress
        self.match = self.hostaddress+"api/v1/face/matchrecord/sync"

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def get_header(self, new_sign):
        timestamp = get_time_stamp()
        sign = to_md5_str(new_sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    def api_face_matchrecord_sync(self, body,sign_only="/api/v1/face/matchrecord/sync"):####
        """刷脸记录同步接口"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.match,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res

if __name__ == '__main__':
    body = {}
    MatchRecord().api_face_matchrecord_sync(body)