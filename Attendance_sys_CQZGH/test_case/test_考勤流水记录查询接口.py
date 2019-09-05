#!/usr/bin/python3
# Time : 2019/8/23 15:29 
# Author : zcl
import pytest
import json,sys
# sys.path.append(r"D:\workfile\zhongkeyuan_workspace")
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *


# @pytest.mark.skip(reason="考勤流水查询")
def test_attendence_record_query():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_record_query(
        reqId=get_uuid(),  # 32位UUID	是
        name="",  # 员工名称	否
        personCode="",  # 员工编码	否
        pageNum=1,  # 分页的起始页，从1开始	是
        pageSize=100,  # 分页的大小	是
        isCount=1,  # 为1表是返回总数	是
        deptId="",  # 部门ID，为空字符串，表示所有部门	是
        startTime="20190827",  # yyyyMMdd	是
        endTime="20190827",  # yyyyMMdd	是
    )
    logger.info(res.text)

    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


if __name__ == '__main__':
    pytest.main(["-s", "test_考勤流水记录查询接口.py"])
