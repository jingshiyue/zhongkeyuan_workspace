#!/usr/bin/python3
# Time : 2019/8/23 15:29 
# Author : zcl
import pytest
import json,sys
sys.path.append(r"D:\workfile\zhongkeyuan_workspace")
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *


# @pytest.mark.skip(reason="考勤规则增加")
def test_attendence_rule_add():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_record_export(
        reqId="",  # 32位UUID	是
        name="",  # 员工名称	否
        personCode="",  # 员工编码	否
        pageNum="",  # 分页的起始页，从1开始	是
        pageSize="",  # 分页的大小	是
        isCount="",  # 为1表是返回总数	是
        deptId="",  # 部门ID，为空字符串，表示所有部门	是
        startTime="",  # yyyyMMdd	是
        endTime="",  # yyyyMMdd	是
    )
    logger.info(res.text)

    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)

