#!/usr/bin/python3
# Time : 2019/8/29 15:03 
# Author : zcl
import pytest
import json,sys
sys.path.append(r"D:\workfile\zhongkeyuan_workspace")
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *


@pytest.mark.skip(reason="考勤导出")
def test_attendence_record_export():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_record_export(
        reqId=get_uuid(),  # 必须 32位UUID
        serialNum="123",  # 必须 导出唯一编号
        exportName="考勤统计",  # 必 须导出的名称
        startTime="20190801",  # 必须 开始日期 yyyyMMdd
        endTime="20190830",  # 必须 结束日期 yyyyMMdd
        deptId="4028858f6ccd13c0016ccd1a88a3000b",  # 必须 部门的ID，为空字符串表示所有部门
    )
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="考勤流水-导出下载")
def test_attendence_record_download():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_record_download(
                            fileName="20190801-20190830考勤统计.xlsx",  #这个参数需先用考勤导出接口的结果得到
                            reqId=get_uuid(),  # 必须 32位UUID
                            serialNum="123")  # 必须 导出唯一编号
    logger.info(res.content)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)



if __name__ == '__main__':
    pytest.main(["-s", "test_考勤导出和进度查询.py"])
