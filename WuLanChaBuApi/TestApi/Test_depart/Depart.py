# coding:utf-8
from WuLanChaBuApi.TestApi.new_method import *
import requests


class Depart(object):
    """部门信息CRUD"""
    def __init__(self,host = "http://192.168.5.15:10019/"):
        """部门信息CRUD"""
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.hostaddress = host
        self.save = self.hostaddress+"api/v1/system/department/save"
        self.update = self.hostaddress+"api/v1/system/department/update"
        self.delete = self.hostaddress+"api/v1/system/department/delete"
        self.query = self.hostaddress+"api/v1/system/department/query"
        self.detail = self.hostaddress+"api/v1/system/department/detail"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def get_header(self, new_sign):
        timestamp = get_time_stamp()
        sign = to_md5_str(new_sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    def api_system_department_save(self, body, sign_only="/api/v1/system/department/save"):
        """增加部门"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.save,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res

    def api_system_department_update(self, body, sign_only="/api/v1/system/department/update"):
        """更新部门"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.update,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_system_department_delete(self, body, sign_only="/api/v1/system/department/delete"):
        """删除部门"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.delete,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_system_department_query(self, body, sign_only="/api/v1/system/department/query"):
        """部门信息查询"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.query,
                            headers=header,
                            json=body,
                            verify=False
                            )
        return res.text

    def api_system_department_detail(self, body, sign_only="/api/v1/system/department/detail"):
        """部门详情查询"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.detail,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text


if __name__ == '__main__':
    depart = Depart()
    body = {"reqId":get_uuid()}
    depart.api_system_department_save(body)
