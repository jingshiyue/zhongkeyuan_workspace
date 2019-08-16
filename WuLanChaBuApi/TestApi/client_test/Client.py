# coding:utf-8
from WuLanChaBuApi.TestApi.new_method import *
import requests


class Client(object):
    def __init__(self):
        """客户端相关接口"""
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.hostaddress = "http://192.168.1.105:9009/face-door-guard/"
        self.regist = self.hostaddress+"api/v1/client/regist"
        self.push = self.hostaddress+"api/v1/client/push/syncdata"
        self.ask_syncdata = self.hostaddress+"api/v1/client/ask/syncdata"
        self.pull = self.hostaddress+"api/v1/client/pull/syncdata"
        self.confirm = self.hostaddress+"api/v1/client/confirm/syncdata"
        self.pull_alldata = self.hostaddress+"api/v1/client/pull/alldata"
        self.delete_alldata = self.hostaddress+"api/v1/client/delete/alldata"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def get_header(self, new_sign):
        timestamp = get_time_stamp()
        sign = to_md5_str(new_sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    def api_client_regist(self, body, sign_only="/api/v1/client/regist"):
        """3.3.1客户端向服务器注册接口
           根据客户端发送过来的设备ID，查询是否在1.2设备表里面，在则返回表1.3里面对应的库ID信息。
           如该设备在表1.2里面查询不到，则返回未授权"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.regist,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_client_push_syncdata(self, body, sign_only="/api/v1/client/push/syncdata"):
        """3.3.2客户端向服务器同步人脸信息接口
           客户端向服务器同步增量的人脸数据，如果发现客户端上传的deviceCode不存在，
           则不接受该客户端发过来的同步请求，返回相应的错误码。
           单次同步的数据，不超过200个，个数服务器可配置。"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.push,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_client_ask_syncdata(self, body, sign_only="/api/v1/client/ask/syncdata"):
        """3.3.3客户端询问服务器是否有对应的增量信息接口
           传输底库ID，设备Code。该接口同时作为心跳接口，检测设备是否断线。
           返回的增量信息，如果是删除的，客户端本地删除后，需要向服务器发送确认消息。"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.ask_syncdata,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_client_pull_syncdata(self, body, sign_only="/api/v1/client/pull/syncdata"):
        """3.3.4客户端请求服务器增量人脸数据接口,客户端向服务器拉去增量数据，建议一次行不操作200，如超过了200条，返回相应的错误码"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.pull,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_client_confirm_syncdata(self, body, sign_only="/api/v1/client/confirm/syncdata"):
        """3.3.5客户端确认服务器增量数据的接口,通过客户端传输过来的增量数据表的ID，删除对应的增量数据表的记录"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.confirm,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_client_pull_alldata(self, body, sign_only="/api/v1/client/pull/alldata"):
        """3.3.6客户端请求服务器全部底库同步接口,客户端向服务器拉取所有的数据，通过分页拉取，建议每页不操作200条记录
            每次只允许拉取一个底库的值"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.pull_alldata,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

    def api_v1_client_delete_alldata(self, body, sign_only="/api/v1/client/delete/alldata"):
        """3.3.7客户端请求清空对应的增量信息表,客户端要求服务器清空对应的增量信息表。
                例如：客户端调用了全部拉取人脸信息，就可以不必管增量数据表，直接调用清空命令"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.delete_alldata,
                            headers=header,
                            json=body,
                            verify=False
                            )
        print(res.text)
        return res.text

if __name__ == '__main__':

    body = {"reqId": get_uuid(),
                "deviceCode": "1",
                "areaCode": "1",
                }
    # Client().api_client_regist(body)

