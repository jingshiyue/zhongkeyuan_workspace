# coding:utf-8
import requests
from WuLanChaBuApi.TestApi.new_method import *


class Regist(object):
    """人脸信息CRUD"""
    def __init__(self,host = "http://172.18.2.128:10010/"):
        """人脸信息CRUD"""
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.hostaddress = host + "face-bussiness-server/"
        self.regist = self.hostaddress+"api/v1/face/regist"
        self.update = self.hostaddress+"api/v1/face/update"
        self.delete = self.hostaddress+"api/v1/face/delete"
        self.query = self.hostaddress+"api/v1/face/query"
        self.detail = self.hostaddress+"api/v1/face/detail"
        self.binding = self.hostaddress+"api/v1/face/lib/binding"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def get_header(self, new_sign):
        timestamp = get_time_stamp()
        sign = to_md5_str(new_sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    def api_v1_face_regist(self, body, sign_only="/api/v1/face/regist"):
        """注册人脸
        上海有机所修改接口
            1.主要用来进行访客的登记。
            2.兼容多条记录的导入
        
        """
        header = self.get_header(sign_only)
        print(self.regist)
        res = requests.post(url=self.regist,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res

    def api_v1_face_update(self, body, sign_only="/api/v1/face/update"):
        """更新人脸信息接口"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.update,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_face_delete(self, body, sign_only="/api/v1/face/delete"):
        """删除人脸信息接口
            上海有机所修改的接口:
                1.只能删除访客的人员信息。
                2.服务器需要进行传入的员工编号进行校验是否是访客人员
        """
        header = self.get_header(sign_only)
        res = requests.post(url=self.delete,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res.text

    def api_v1_face_query(self, body, sign_only="/api/v1/face/query"):
        """查询人脸信息接口"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.query,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_face_detail(self, body, sign_only="/api/v1/face/detail"):
        """详情查询人脸信息接口"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.detail,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_face_lib_binding(self, body, sign_only="/api/v1/face/lib/binding"):
        """人脸信息与人脸库的绑定"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.binding,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res

if __name__ == '__main__':
    regist = Regist()
    body = {}
    regist.api_v1_face_update(body)