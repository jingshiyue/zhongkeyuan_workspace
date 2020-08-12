# coding:utf-8
from WuLanChaBuApi.TestApi.new_method import *
import requests


class FaceLib(object):
    def __init__(self,host="http://172.18.2.199:10019/"):
        """人脸底库的CRUD接口"""
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.hostaddress = host
        self.create = self.hostaddress + "api/v1/system/facelib/create"
        self.update = self.hostaddress + "api/v1/system/facelib/update"
        self.delete = self.hostaddress + "api/v1/system/facelib/delete"
        self.query = self.hostaddress + "api/v1/system/facelib/query"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def get_header(self, new_sign):
        timestamp = get_time_stamp()
        sign = to_md5_str(new_sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    def api_v1_facelib_create(self, body,sign_only="/api/v1/system/facelib/create"):
        """底库创建"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.create,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res

    def api_v1_facelib_update(self, body, sign_only="/api/v1/system/facelib/update"):
        """底库更新"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.update,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_facelib_delete(self, body, sign_only="/api/v1/system/facelib/delete"):
        """底库删除"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.delete,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_facelib_query(self, body, sign_only="/api/v1/system/facelib/query"):
        """底库删除"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.query,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res.text


if __name__ == '__main__':
    facelib = FaceLib()
    body = {"reqId":get_uuid()}
    facelib.api_v1_facelib_create(body)