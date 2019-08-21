#!/usr/bin/python3
# Time : 2019/8/21 17:44 
# Author : zcl
import pytest
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import attendance_sys
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()

def test_01():
    res = attendance_sys().api_v1_attendence_rule_save()
    logger.info(res.text)








if __name__ == '__main__':
    pytest.main(["-q", "test_考勤规则相关接口.py"])