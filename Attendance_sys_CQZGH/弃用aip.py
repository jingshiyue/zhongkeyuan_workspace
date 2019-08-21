#!/usr/bin/python3
# Time : 2019/8/21 15:10
# Author : zcl
import requests

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