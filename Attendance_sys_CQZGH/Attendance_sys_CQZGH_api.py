#!/usr/bin/python3
# Time : 2019/8/15 17:23 
# Author : zcl
import requests
from Attendance_sys_CQZGH.utils.common_method import *
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()


class attendance_sys():
    def __init__(self, host="http://192.168.5.15:10019/",server=""):
        self.host = host
        self.server = server
        self._api_v1_attendence_rule_save = self.host + self.server + "api/v1/attendence/rule/save"
        self._api_v1_attendence_rule_update = self.host + self.server + "api/v1/attendence/rule/update"
        self._api_v1_attendence_rule_update = self.host + self.server + "api/v1/attendence/rule/update"
        self._api_v1_attendence_rule_delete = self.host + self.server + "api/v1/attendence/rule/delete"
        self._api_v1_attendence_rule_query = self.host + self.server + "api/v1/attendence/rule/query"
        self._api_v1_attendence_leave_save = self.host + self.server + "api/v1/attendence/leave/save"
        self._api_v1_attendence_leave_update = self.host + self.server + "api/v1/attendence/leave/update"
        self._api_v1_attendence_leave_query = self.host + self.server + "api/v1/attendence/leave/query"
        self._api_v1_attendence_leave_delete = self.host + self.server + "api/v1/attendence/leave/delete"
        self._api_v1_attendence_businessout_save = self.host + self.server + "api/v1/attendence/businessout/save"
        self._api_v1_attendence_businessout_update = self.host + self.server + "api/v1/attendence/businessout/update"
        self._api_v1_attendence_businessout_query = self.host + self.server + "api/v1/attendence/businessout/query"
        self._api_v1_attendence_businessout_delete = self.host + self.server + "api/v1/attendence/businessout/delete"
        self._api_v1_attendence_temporaryout_save = self.host + self.server + "api/v1/attendence/temporaryout/save"
        self._api_v1_attendence_temporaryout_update = self.host + self.server + "api/v1/attendence/temporaryout/update"
        self._api_v1_attendence_temporaryout_query = self.host + self.server + "api/v1/attendence/temporaryout/query"
        self._api_v1_attendence_temporaryout_query = self.host + self.server + "api/v1/attendence/temporaryout/query"
        self._api_v1_attendence_repunching_save = self.host + self.server + "api/v1/attendence/repunching/save"
        self._api_v1_attendence_repunching_query = self.host + self.server + "api/v1/attendence/repunching/query"
        self._api_v1_attendence_record_query = self.host + self.server + "api/v1/attendence/record/query"
        self._api_v1_attendence_record_export = self.host + self.server + "api/v1/attendence/record/export"
        self._api_v1_attendence_record_export_progress = self.host + self.server + "api/v1/attendence/record/export/progress"
        self._api_v1_attendence_special_save = self.host + self.server + "/api/v1/attendence/special/save"
        self._api_v1_attendence_special_update = self.host + self.server + "/api/v1/attendence/special/update"
        self._api_v1_attendence_special_query = self.host + self.server + "/api/v1/attendence/special/query"
        self._api_v1_attendence_special_delete = self.host + self.server + "/api/v1/attendence/special/delete"

    def get_headers(self,sign):
        """
        sing:"/api/v1/face/backlist/save""
        """
        logger.info(sign)
        apiId = "123456"
        apiKey = "1285384ddfb057814bad78127bc789be"
        timestamp = get_time_stamp()
        sign = to_md5_str(sign + timestamp + apiKey)
        header = {"apiId": apiId, "sign": sign, "timestamp": ""}

        logger.info(sign)
        logger.info(timestamp)

        return header


    """3.9.1.1考勤规则增加接口"""
    def api_v1_attendence_rule_save(self,
                                    reqId=get_uuid(),
                                    ruleName = "AM",  # 规则名称  {"0":"AM-早上","1":"AMLate-早上迟到","2":"NM-中午","3":"NMLate-中午迟到","4":"PM-下午","5":"PMLate-下午迟到"}
                                    startTime = "083000",  # 开始时间HHmmss
                                    endTime = "090000", # 结束时间HHmmss
                                    ):
        body = {
            "reqId": reqId,
            "ruleName": ruleName,
            "startTime": startTime,
            "endTime": endTime
        }
        res = requests.post(url=self._api_v1_attendence_rule_save,
                            json=body,
                           headers=self.get_headers("/api/v1/attendence/rule/save")
                            )
        res.close()
        return res

    """3.9.1.2考勤规则更新接口"""
    def api_v1_attendence_rule_update(self,
                                      reqId=get_uuid(),#必须
                                      id="",  # 必须  需要修改的规则的ID
                                      startTime="083000",  #必须 开始时间HHmmss
                                      endTime="090000"):  #必须 结束时间HHmmss

        body = {
            "reqId": reqId,
            "id": id,
            "startTime": startTime,
            "endTime": endTime
        }

        res = requests.post(url=self._api_v1_attendence_rule_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/update"),
                            )
        res.close()
        return res

    """3.9.1.3考勤规则删除接口（不建议使用）"""
    def api_v1_attendence_rule_delete(self,
                                      reqId=get_uuid(),
                                      ids=""):  # 设备id，支持逗号“，”隔开

        body = {
            "reqId": reqId,
            "ids": ids,
        }
        res = requests.post(url=self._api_v1_attendence_rule_delete,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/delete"),
                            )
        res.close()
        return res


    """3.9.1.4考勤规则查询接口"""

    def api_v1_attendence_rule_query(self,
                                      reqId=get_uuid()):
        logger.info(len(reqId))
        body = {
            "reqId": reqId
        }
        res = requests.post(url=self._api_v1_attendence_rule_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/rule/query"),
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
        res = requests.post(url=self._api_v1_attendence_record_query,
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
        res = requests.post(url=self._api_v1_attendence_record_export,
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
        res = requests.post(url=self._api_v1_attendence_record_export_progress,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/record/export/progress"),
                            )
        res.close()
        return res


    """考勤登记-增加接口"""
    def api_v1_attendence_special_save(self,
                                       reqId=get_uuid(),  # 必须		32位UUID
                                       personCode="",  # 必须		员工编码
                                       faceName="",  # 必须		员工姓名
                                       deptName="",  # 必须		部门名称
                                       deptId="",  # 必须		部门ID
                                       facePersonSex="",  # 必须		员工性别
                                       recordType="",  # 必须		0-请假，1-公务外出，2-临时外出，3-补卡
                                       startTime="",  # 必须		开始时间yyyyMMddHHmmss
                                       endTime="",  # 必须		结束时间yyyyMMddHHmmss
                                       remark="",  # 必须		备注
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
        res = requests.post(url=self._api_v1_attendence_special_save,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/special/save"),
                            )
        res.close()
        return res



    """考勤登记-更新接口"""
    def api_v1_attendence_special_update(self,
                                       reqId=get_uuid(),  # 必须		32位UUID
                                       id="",# 必须
                                       startTime="",  # 必须		开始时间yyyyMMddHHmmss
                                       endTime="",  # 必须		结束时间yyyyMMddHHmmss
                                       remark="",  # 必须		备注
                                       ):
        body = {
            "reqId": reqId,
            "id":id,
            "startTime": startTime,
            "endTime": endTime,
            "remark": remark,
        }
        res = requests.post(url=self._api_v1_attendence_special_update,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/special/update"),
                            )
        res.close()
        return res



    """考勤登记-查询接口"""
    def api_v1_attendence_special_query(self,
                                        reqId="",  # 必须    32位UUID
                                        name="",  # 非必须    员工姓名
                                        personCode="",  # 非必须    员工编码
                                        pageNum="",  # 必须    页码
                                        pageSize="",  # 必须    页大小
                                        recordType="",  # 非必须    0-请假，1-公务外出，2-临时外出，3-补卡
                                        isCount="",  # 必须    为1表是返回总数
                                        startTime="",  # 必须    开始时间yyyyMMdd
                                        endTime="",  # 必须    结束时间yyyyMMdd
                                        deptId="",  # 必须    部门ID，为空字符串，表示所有部门
                                        ):
        body = {
            "reqId": reqId,
            "name": name,
            "personCode": personCode,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "recordType": recordType,
            "isCount": isCount,
            "startTime": startTime,
            "endTime": endTime,
            "deptId": deptId,
        }
        res = requests.post(url=self._api_v1_attendence_special_query,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/special/query"),
                            )
        res.close()
        return res



    """考勤登记-查询接口"""
    def api_v1_attendence_special_delete(self,
                                         reqId="",  # 必须		32位UUID
                                         ids="",  # 必须
                                         ):
        body = {
            "reqId": reqId,
            "ids": ids,
        }
        res = requests.post(url=self._api_v1_attendence_special_delete,
                            json=body,
                            headers=self.get_headers("/api/v1/attendence/special/delete"),
                            )
        res.close()
        return res

if __name__ == '__main__':
    res = attendance_sys().api_v1_attendence_rule_query()
    print(res.text)