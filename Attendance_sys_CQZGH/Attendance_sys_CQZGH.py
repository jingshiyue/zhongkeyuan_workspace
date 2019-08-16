#!/usr/bin/python3
# Time : 2019/8/15 17:23 
# Author : zcl
import requests
from utils.common_method import *


class attendance_sys():
    def __init__(self, host="http://192.168.5.15:4433/"):
        self.anjian_server = ""
        self.api_v1_attendence_rule_save = self.host + self.anjian_server + "/api/v1/face/security/ticket-check"
        self.api_v1_attendence_rule_update = ""


    """3.9.1.1考勤规则增加接口"""
    def api_v1_attendence_rule_save(self,
                                    reqId=get_uuid(),
                                    ruleName = "AM",  # 规则名称
                                    startTime = "083000",  # 开始时间HHmmss
                                    endTime = "090000"): # 结束时间HHmmss

        body = {
            "reqId": reqId,
            "ruleName": ruleName,
            "startTime": startTime,
            "endTime": endTime
        }

        res = requests.post(url=self.api_v1_attendence_rule_save,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/save"),
                            )
        res.close()
        return res

    """3.9.1.2考勤规则更新接口"""
    def api_v1_attendence_rule_update(self,
                                      reqId=get_uuid(),
                                      id="",  # 需要修改的规则的ID
                                      startTime="083000",  # 开始时间HHmmss
                                      endTime="090000"):  # 结束时间HHmmss

        body = {
            "reqId": reqId,
            "id": id,
            "startTime": startTime,
            "endTime": endTime
        }

        res = requests.post(url=self.api_v1_attendence_rule_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/update"),
                            )
        res.close()
        return res

    """3.9.1.3考勤规则删除接口（不建议使用）"""
    def api_v1_attendence_rule_delete(self,
                                      reqId=get_uuid(),
                                      id=""):  # 设备id，支持逗号“，”隔开

        body = {
            "reqId": reqId,
            "id": id,
        }

        res = requests.post(url=self.api_v1_attendence_rule_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/delete"),
                            )
        res.close()
        return res

    """3.9.1.4考勤规则查询接口"""

    def api_v1_attendence_rule_delete(self,
                                      reqId=get_uuid()):


        body = {
            "reqId": reqId,
            "id": id,
        }

        res = requests.post(url=self.api_v1_attendence_rule_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/query"),
                            )
        res.close()
        return res