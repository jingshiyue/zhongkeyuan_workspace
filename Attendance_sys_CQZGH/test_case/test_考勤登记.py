#!/usr/bin/python3
# Time : 2019/8/23 14:11 
# Author : zcl
import pytest
import json,sys
sys.path.append(r"D:\workfile\zhongkeyuan_workspace")
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *


# @pytest.mark.skip(reason="考勤登记增加")
def test_attendence_rule_add():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_special_save(
        reqId=get_uuid(),  # 必须		32位UUID
        personCode="a001",  # 必须		员工编码
        faceName="西瓜",  # 必须		员工姓名
        deptName="部门01",  # 必须		部门名称
        deptId="123456",  # 必须		部门ID
        facePersonSex=1,  # 必须		员工性别
        recordType=0,  # 必须		0-请假，1-公务外出，2-临时外出，3-补卡
        startTime="20190822083000",  # 必须		开始时间yyyyMMddHHmmss
        endTime="20190822180000",  # 必须		结束时间yyyyMMddHHmmss
        remark="事假",  # 必须		备注
    )
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)

# @pytest.mark.skip(reason="考勤登记查询")
def test_attendence_special_query():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_special_query(
        reqId=get_uuid(),  # 必须    32位UUID
        name="西瓜",  # 非必须    员工姓名
        personCode="a001",  # 非必须    员工编码
        pageNum=1,  # 必须    页码从1开始，到10
        pageSize=10,  # 必须    页大小
        recordType=0,  # 非必须    0-请假，1-公务外出，2-临时外出，3-补卡
        isCount=0,  # 必须    为1表是返回总数,枚举：请假 公务外出 临时外出 补卡
        startTime="20190822",  # 必须    开始时间yyyyMMdd
        endTime="20190823",  # 必须    结束时间yyyyMMdd
        deptId="部门01",  # 必须    部门ID，为空字符串，表示所有部门
    )
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


@pytest.mark.skip(reason="考勤登记更新")
def test_attendence_special_update():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_special_update(
        reqId=get_uuid(),  # 必须		32位UUID
        id="",  # 必须
        startTime="",  # 必须		开始时间yyyyMMddHHmmss
        endTime="",  # 必须		结束时间yyyyMMddHHmmss
        remark="",  # 必须		备注
    )
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


@pytest.mark.skip(reason="考勤登记删除")
def api_v1_attendence_special_delete():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_special_delete(
        reqId=get_uuid(),  # 必须    32位UUID
        ids="",  # 必须
    )
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


if __name__ == '__main__':
    pytest.main(["-v -s", "test_考勤登记.py"])
