#!/usr/bin/python3
# Time : 2019/8/23 14:11 
# Author : zcl
import pytest
import json,sys
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *



# @pytest.mark.skip(reason="考勤登记增加")
def test_attendence_rule_add():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_special_save(
        reqId=get_uuid(),  # 必须		32位UUID
        personCode="500382199001017100",  # 必须		员工编码
        faceName="测试考勤100",  # 必须		员工姓名
        deptName="职工服务中心",  # 必须		部门名称
        deptId="4028858f6ccd13c0016ccd1a88a3000b",  # 必须		部门ID
        facePersonSex=1,  # 必须		员工性别
        recordType="4",  # 必须		0-请假，1-公务外出，2-临时外出，3-补卡； 补卡：填一样的 早上9：00 中午 12点  晚上  18：00
        startTime="20191122090000",  # 必须		开始时间yyyyMMddHHmmss
        endTime="20191122120000",  # 必须		结束时间yyyyMMddHHmmss
        remark="test99" # 必须		备注
    )
    logger.info(res.text)
    assert json.loads(res.text)["status"] == 0
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="考勤登记查询")
def test_attendence_special_query():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_special_query(
        reqId=get_uuid(),  # 必须    32位UUID
        name="",  # 非必须    员工姓名
        personCode="",  # 非必须    员工编码
        pageNum=1,  # 必须    页码从1开始，到10
        pageSize=100,  # 必须    页大小
        recordType="4",  # 非必须    0-请假，1-公务外出，2-临时外出，3-补卡
        isCount=1,  # 必须    为1表示返回总数,枚举：请假 公务外出 临时外出 补卡
        startTime="20191119",  # 必须    开始时间yyyyMMdd
        endTime="20191119",  # 必须    结束时间yyyyMMdd
        deptId="",  # 非必须    部门ID，为空字符串，表示所有部门
    )
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)



@pytest.mark.skip(reason="考勤登记删除")
def test_attendence_special_delete():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_special_delete(
        reqId=get_uuid(),  # 必须    32位UUID
        ids="4028858f6ce0166b016ce0444b1a0010",  # 必须
    )
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


if __name__ == '__main__':
    pytest.main(["-s", "test_考勤登记.py"])
