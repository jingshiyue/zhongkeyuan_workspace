#!/usr/bin/python3
# Time : 2019/8/15 17:23 
# Author : zcl
import requests
from utils.common_method import *

class attendance_sys():
    def __init__(self, host="http://192.168.5.15:4433/"):
        self.host = host
        self.anjian_server = ""
        self.api_v1_attendence_rule_save = self.host + self.anjian_server + "api/v1/attendence/rule/save"
        self.api_v1_attendence_rule_update = self.host + self.anjian_server + "api/v1/attendence/rule/update"
        self.api_v1_attendence_rule_update = self.host + self.anjian_server + "api/v1/attendence/rule/update"
        self.api_v1_attendence_rule_delete = self.host + self.anjian_server + "api/v1/attendence/rule/delete"
        self.api_v1_attendence_rule_query = self.host + self.anjian_server + "api/v1/attendence/rule/query"
        self.api_v1_attendence_leave_save = self.host + self.anjian_server + "api/v1/attendence/leave/save"
        self.api_v1_attendence_leave_update = self.host + self.anjian_server + "api/v1/attendence/leave/update"
        self.api_v1_attendence_leave_query = self.host + self.anjian_server + "api/v1/attendence/leave/query"
        self.api_v1_attendence_leave_delete = self.host + self.anjian_server + "api/v1/attendence/leave/delete"
        self.api_v1_attendence_businessout_save = self.host + self.anjian_server + "api/v1/attendence/businessout/save"
        self.api_v1_attendence_businessout_update = self.host + self.anjian_server + "api/v1/attendence/businessout/update"
        self.api_v1_attendence_businessout_query = self.host + self.anjian_server + "api/v1/attendence/businessout/query"
        self.api_v1_attendence_businessout_delete = self.host + self.anjian_server + "api/v1/attendence/businessout/delete"
        self.api_v1_attendence_temporaryout_save = self.host + self.anjian_server + "api/v1/attendence/temporaryout/save"
        self.api_v1_attendence_temporaryout_update = self.host + self.anjian_server + "api/v1/attendence/temporaryout/update"
        self.api_v1_attendence_temporaryout_query = self.host + self.anjian_server + "api/v1/attendence/temporaryout/query"
        self.api_v1_attendence_temporaryout_query = self.host + self.anjian_server + "api/v1/attendence/temporaryout/query"
        self.api_v1_attendence_repunching_save = self.host + self.anjian_server + "api/v1/attendence/repunching/save"
        self.api_v1_attendence_repunching_query = self.host + self.anjian_server + "api/v1/attendence/repunching/query"
        self.api_v1_attendence_record_query = self.host + self.anjian_server + "api/v1/attendence/record/query"
        self.api_v1_attendence_record_export = self.host + self.anjian_server + "api/v1/attendence/record/export"
        self.api_v1_attendence_record_export_progress = self.host + self.anjian_server + "api/v1/attendence/record/export/progress"

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
        res = requests.post(url=self.api_v1_attendence_rule_delete,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/query"),
                            )
        res.close()
        return res

    """3.9.1.4考勤规则查询接口"""

    def api_v1_attendence_rule_query(self,
                                      reqId=get_uuid()):

        body = {
            "reqId": reqId
        }
        res = requests.post(url=self.api_v1_attendence_rule_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/query"),
                            )
        res.close()
        return res

    """3.9.2.1考勤登记-请假增加接口"""
    def api_v1_attendence_leave_save(self,
                                     reqId=get_uuid(),
                                     personCode="",#员工编码	是
                                     faceName="",#员工姓名	是
                                     deptName="",#部门名称	是
                                     deptId="",#部门ID	是
                                     facePersonSex="",#员工性别	是
                                     recordType="",#0-请假，1-公务外出，2-临时外出，3-补卡	是
                                     startTime="",#开始时间HHmmss	是
                                     endTime="",#结束时间HHmmss	是
                                     remark="",#备注	是
                                     ):
        body = {
                "reqId": reqId,
                "personCode": personCode,
                "faceName": faceName,
                "deptName": deptName,
                "deptId": deptId,
                "facePersonSex": facePersonSex,
                "recordType": recordType,
                "startTime": startTime,
                "endTime": endTime,
                "remark": remark,
        }

        res = requests.post(url=self.api_v1_attendence_leave_save,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/leave/save"),
                            )
        res.close()
        return res

    """3.9.2.2考勤登记-请假修改接口"""
    def api_v1_attendence_leave_update(self,
                                     reqId=get_uuid(),
                                     id = "",#请假的ID  是
                                     startTime="",  # 开始时间HHmmss	是
                                     endTime="",  # 结束时间HHmmss	是
                                     remark="",  # 备注	是
                                     ):
        body = {
            "reqId":reqId,
            "id":id,
            "startTime":startTime,
            "endTime":endTime,
            "remark":remark,
        }
        res = requests.post(url=self.api_v1_attendence_leave_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/leave/update"),
                            )
        res.close()
        return res

    """3.9.2.3考勤登记-请假查询接口"""
    def api_v1_attendence_leave_query(self,
                                      reqId=get_uuid(),  # 32位UUID  是
                                      name="西瓜",  # 员工名称	否
                                      personCode="",  # 员工编码	否
                                      pageNum="",  # 分页的起始页，从1开始	是
                                      pageSize="",  # 分页的大小	是
                                      isCount="",  # 为1表是返回总数	是
                                      deptId="",  # 部门ID，为空字符串，表示所有部门 是
                                      startTime="",  # yyyyMMdd	是
                                      endTime="",  # yyyyMMdd 是
                                      ):
        body = {
            "reqId": reqId,
            "name": name,
            "personCode": personCode,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "isCount": isCount,
            "deptId": deptId,
            "startTime": startTime,
            "endTime": endTime
        }
        res = requests.post(url=self.api_v1_attendence_leave_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/leave/query"),
                            )
        res.close()
        return res


    """3.9.2.3考勤登记-请假查询接口"""
    def api_v1_attendence_leave_delete(self,
                                      reqId=get_uuid(),  # 32位UUID  是
                                      ids = ""#设备id，支持逗号“，”隔开  是
                                      ):
        body = {
            "reqId": reqId,
            "ids":ids
        }
        res = requests.post(url=self.api_v1_attendence_leave_delete,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/leave/delete"),
                            )
        res.close()
        return res

    """3.9.2.5考勤登记-公务外出增加接口"""
    def api_v1_attendence_businessout_save(self,
                                           reqId=get_uuid(),  # 32位UUID	是
                                           personCode="",  # 员工编码	是
                                           faceName="",  # 员工姓名	是
                                           deptName="",  # 部门名称	是
                                           deptId="",  # 部门ID	是
                                           facePersonSex="",  # 员工性别	是
                                           recordType="",  # 0-请假，1-公务外出，2-临时外出，3-补卡	是
                                           startTime="",  # 开始时间HHmmss	是
                                           endTime="",  # 结束时间HHmmss	是
                                           remark=""  # 备注	是
                                           ):
        body = {
            "reqId": reqId,
            "personCode": personCode,
            "faceName": faceName,
            "deptName": deptName,
            "deptId": deptId,
            "facePersonSex": facePersonSex,
            "recordType": recordType,
            "startTime": startTime,
            "endTime": endTime,
            "remark": remark
        }
        res = requests.post(url=self.api_v1_attendence_businessout_save,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/businessout/save"),
                            )
        res.close()
        return res

    """3.9.2.6考勤登记-公务外出修改接口"""
    def api_v1_attendence_businessout_update(self,
                                             reqId=get_uuid(),  # 32位UUID	是
                                             id="",  # 请假的ID	是
                                             startTime="",  # 开始时间HHmmss	是
                                             endTime="",  # 结束时间HHmmss	是
                                             remark="",  # 备注	是
                                             ):
        body = {
            "reqId": reqId,
            "id": id,
            "startTime": startTime,
            "endTime": endTime,
            "remark": remark,
        }
        res = requests.post(url=self.api_v1_attendence_businessout_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/ businessout/update"),
                            )
        res.close()
        return res

    """3.9.2.7考勤登记-公务外出查询接口"""
    def api_v1_attendence_businessout_query(self,
                                             reqId="",  # 32位UUID	是
                                             name="",  # 员工名称	否
                                             personCode="",  # 员工编码	否
                                             pageNum="",  # 分页的起始页，从1开始	是
                                             pageSize="",  # 分页的大小	是
                                             isCount="",  # 为1表是返回总数	是
                                             deptId="",  # 部门ID，为空字符串，表示所有部门	是
                                             startTime="",  # yyyyMMdd	是
                                             endTime="",  # yyyyMMdd	是
                                             ):
        body = {
            "reqId": reqId,
            "name": name,
            "personCode": personCode,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "isCount": isCount,
            "deptId": deptId,
            "startTime": startTime,
            "endTime": endTime,
        }
        res = requests.post(url=self.api_v1_attendence_businessout_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/businessout/query"),
                            )
        res.close()
        return res

    """3.9.2.8考勤登记-公务外出删除接口"""
    def api_v1_attendence_businessout_delete(self,
                                             reqId=get_uuid(),  # 32位UUID	是
                                             ids=""#设备id，支持逗号“，”隔开   是
                                             ):
        body = {
            "reqId": reqId,
            "ids":ids
        }
        res = requests.post(url=self.api_v1_attendence_businessout_delete,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/businessout/delete"),
                            )
        res.close()
        return res

    """3.9.2.9考勤登记-临时外出增加接口"""
    def api_v1_attendence_temporaryout_save(self,
                                            reqId=get_uuid(),  # 32位UUID	是
                                            personCode="",  # 员工编码	是
                                            faceName="",  # 员工姓名	是
                                            deptName="",  # 部门名称	是
                                            deptId="",  # 部门ID	是
                                            facePersonSex="",  # 员工性别	是
                                            recordType="",  # 0-请假，1-公务外出，2-临时外出，3-补卡	是
                                            startTime="",  # 开始时间HHmmss	是
                                            endTime="",  # 结束时间HHmmss	是
                                            remark="",  # 备注	是

                                            ):
        body = {
            "reqId": reqId,
            "personCode": personCode,
            "faceName": faceName,
            "deptName": deptName,
            "deptId": deptId,
            "facePersonSex": facePersonSex,
            "recordType": recordType,
            "startTime": startTime,
            "endTime": endTime,
            "remark": remark

        }
        res = requests.post(url=self.api_v1_attendence_temporaryout_save,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/temporaryout/save"),
                            )
        res.close()
        return res

    """3.9.2.10考勤登记-临时外出修改接口"""
    def api_v1_attendence_temporaryout_update(self,
                                              reqId=get_uuid(),  # 32位UUID	是
                                              id="",  # 请假的ID	是
                                              startTime="",  # 开始时间HHmmss	是
                                              endTime="",  # 结束时间HHmmss	是
                                              remark="",  # 备注	是
                                              ):
        body = {
            "reqId":reqId,
            "id":id,
            "startTime":startTime,
            "endTime":endTime,
            "remark":remark
        }
        res = requests.post(url=self.api_v1_attendence_temporaryout_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/temporaryout/update"),
                            )
        res.close()
        return res

    """3.9.2.11考勤登记-临时外出查询接口"""
    def api_v1_attendence_temporaryout_query(self,
                                             reqId="",  # 32位UUID	是
                                             name="",  # 员工名称	否
                                             personCode="",  # 员工编码	否
                                             pageNum="",  # 分页的起始页，从1开始	是
                                             pageSize="",  # 分页的大小	是
                                             isCount="",  # 为1表是返回总数	是
                                             deptId="",  # 部门ID，为空字符串，表示所有部门	是
                                             startTime="",  # yyyyMMdd	是
                                             endTime="",  # yyyyMMdd	是
                                             ):
        body = {
            "reqId": reqId,
            "name": name,
            "personCode": personCode,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "isCount": isCount,
            "deptId": deptId,
            "startTime": startTime,
            "endTime": endTime
        }
        res = requests.post(url=self.api_v1_attendence_temporaryout_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/temporaryout/query"),
                            )
        res.close()
        return res

    """3.9.2.12考勤登记-临时外出删除接口"""
    def api_v1_attendence_temporaryout_delete(self,
                                             reqId="",  # 32位UUID	是
                                             ids=""# 设备id，支持逗号“，”隔开
                                             ):
        body = {
            "reqId": reqId,
            "ids":ids
        }
        res = requests.post(url=self.api_v1_attendence_temporaryout_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/temporaryout/delete"),
                            )
        res.close()
        return res

    """3.9.2.13考勤登记-补卡增加接口"""
    def api_v1_attendence_repunching_save(self,
                                          reqId="",  # 32位UUID	是
                                          personCode="",  # 员工编码	是
                                          faceName="",  # 员工姓名	是
                                          deptName="",  # 部门名称	是
                                          deptId="",  # 部门ID	是
                                          facePersonSex="",  # 员工性别	是
                                          recordType="",  # 0-请假，1-公务外出，2-临时外出，3-补卡	是
                                          startTime="",  # 开始时间HHmmss	是
                                          endTime="",  # 结束时间HHmmss	是
                                          remark="",  # 备注	是
                                          ):
        body = {
            "reqId":reqId,
            "personCode":personCode,
            "faceName":faceName,
            "deptName":deptName,
            "deptId":deptId,
            "facePersonSex":facePersonSex,
            "recordType":recordType,
            "startTime":startTime,
            "endTime":endTime,
            "remark":remark,
        }
        res = requests.post(url=self.api_v1_attendence_repunching_save,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/repunching/save"),
                            )
        res.close()
        return res

    """3.9.2.14考勤登记-补卡查询接口"""
    def api_v1_attendence_repunching_query(self,
                                          reqId="",  # 32位UUID	是
                                          name="",  # 员工名称	否
                                          personCode="",  # 员工编码	否
                                          pageNum="",  # 分页的起始页，从1开始	是
                                          pageSize="",  # 分页的大小	是
                                          isCount="",  # 为1表是返回总数	是
                                          deptId="",  # 部门ID，为空字符串，表示所有部门	是
                                          startTime="",  # yyyyMMdd	是
                                          endTime="",  # yyyyMMdd	是
                                          ):
        body = {
            "reqId":reqId,
            "name":name,
            "personCode":personCode,
            "pageNum":pageNum,
            "pageSize":pageSize,
            "isCount":isCount,
            "deptId":deptId,
            "startTime":startTime,
            "endTime":endTime,
        }
        res = requests.post(url=self.api_v1_attendence_repunching_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/repunching/query"),
                            )
        res.close()
        return res

    """3.9.3考勤流水记录查询接口"""
    def api_v1_attendence_record_query(self,
                                       reqId="",  # 32位UUID	是
                                       name="",  # 员工名称	否
                                       personCode="",  # 员工编码	否
                                       pageNum="",  # 分页的起始页，从1开始	是
                                       pageSize="",  # 分页的大小	是
                                       isCount="",  # 为1表是返回总数	是
                                       deptId="",  # 部门ID，为空字符串，表示所有部门	是
                                       startTime="",  # yyyyMMdd	是
                                       endTime="",  # yyyyMMdd	是
                                           ):
        body = {
            "reqId":reqId,
            "name":name,
            "personCode":personCode,
            "pageNum":pageNum,
            "pageSize":pageSize,
            "isCount":isCount,
            "deptId":deptId,
            "startTime":startTime,
            "endTime":endTime,
        }
        res = requests.post(url=self.api_v1_attendence_record_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/record/query"),
                            )
        res.close()
        return res

    """3.9.4考勤记录导出接口"""
    def api_v1_attendence_record_export(self,
                                        reqId="",  # 32位UUID	是
                                        serialNum="",  # 唯一的标志序列号	是
                                        exportName="",  # 需要导出数据的记录名称	是
                                        startTime="",  # 开始时间yyyyMMdd	是
                                        endTime="",  # 结束时间yyyyMMdd	是
                                        deptId="",  # 部门的ID，为空字符串表示所有部门	是
                                        ):
        body = {
            "reqId":reqId,
            "serialNum":serialNum,
            "exportName":exportName,
            "startTime":startTime,
            "endTime":endTime,
            "deptId":deptId
        }
        res = requests.post(url=self.api_v1_attendence_record_export,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/record/export"),
                            )
        res.close()
        return res

    """3.9.5考勤记录导出文件进度查询"""
    def api_v1_attendence_record_export_progress(self,
                                        reqId="",  # 32位UUID	是
                                        serialNum="",  # 序列号
                                        ):
        body = {
            "reqId":reqId,
            "serialNum":serialNum,
        }
        res = requests.post(url=self.api_v1_attendence_record_export_progress,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/record/export/progress"),
                            )
        res.close()
        return res

