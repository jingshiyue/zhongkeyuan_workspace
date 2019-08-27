#!/usr/bin/python3
# Time : 2019/8/21 17:44 
# Author : zcl   D:\workfile\zhongkeyuan_workspace\Attendance_sys_CQZGH\test_case\test_考勤规则相关接口.py

import pytest
import json,sys
# sys.path.append(r"D:\workfile\zhongkeyuan_workspace")
from zhongkeyuan_workspace.Attendance_sys_CQZGH.utils.common_method import *
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import attendance_sys
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()


# @pytest.mark.skip(reason="考勤规则增加")
# def test_attendence_rule_add():
#     logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
#     res = attendance_sys().api_v1_attendence_rule_save(ruleName="PM-下午",startTime="140000",endTime="180000")
#     logger.info(res.text)
#     data_json = json.loads(res.text)
#
#     res = attendance_sys().api_v1_attendence_rule_query()
#     logger.info(res.text)
#     logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="考勤规则查询")
def test_attendence_rule_query():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_rule_query(
                                                        reqId = get_uuid())
    logger.info(res.text)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="测试考勤规则更新流程[添加规则->查询规则->更新规则->验证规则更新成功否->规则更改回去]")
# def test_attendence_rule_update():
#     logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
#     res = attendance_sys().api_v1_attendence_rule_save(ruleName="AMLate")
#     logger.info(res.text)
#     res = attendance_sys().api_v1_attendence_rule_query()
#     logger.info(res.text)
#     id = json.loads(res.text)["results"][0]["id"]
#     ruleName = json.loads(res.text)["results"][0]["ruleName"]
#     startTime = json.loads(res.text)["results"][0]["startTime"]
#     endTime = json.loads(res.text)["results"][0]["endTime"]
#     logger.info("******************")
#     logger.info(json.loads(res.text)["results"][0])
#     logger.info(json.loads(res.text)["results"][0]["id"])
#     logger.info(startTime)
#     logger.info(endTime)
#     logger.info("******************")
#     res = attendance_sys().api_v1_attendence_rule_update(id=id,startTime="111111",endTime="111112")
#     logger.info(res.text)
#     res = attendance_sys().api_v1_attendence_rule_query()
#     logger.info(json.loads(res.text)["results"])
#
#     res = attendance_sys().api_v1_attendence_rule_update(id=id, startTime=startTime, endTime=endTime)
#     logger.info(res.text)
#     res = attendance_sys().api_v1_attendence_rule_query()
#     logger.info(json.loads(res.text)["results"])
#     logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)
#
#
# @pytest.mark.skip(reason="测试考勤删除[包含了些流程，查询->删除]")
# def test_attendence_rule_delete():
#     logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
#     res = attendance_sys().api_v1_attendence_rule_query()
#     id = json.loads(res.text)["results"][0]["id"]
#     ruleName = json.loads(res.text)["results"][0]["ruleName"]
#     startTime = json.loads(res.text)["results"][0]["startTime"]
#     endTime = json.loads(res.text)["results"][0]["endTime"]
#     logger.info("******************")
#     logger.info(json.loads(res.text)["results"][0])
#     logger.info(json.loads(res.text)["results"][0]["id"])
#     logger.info(startTime)
#     logger.info(endTime)
#     logger.info("******************")
#
#     res = attendance_sys().api_v1_attendence_rule_delete(ids=id)
#     logger.info(res.text)
#     res = attendance_sys().api_v1_attendence_rule_query()
#     logger.info(json.loads(res.text)["results"])
#     logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)
#

if __name__ == '__main__':
    pytest.main(["-v -s", "test_考勤规则相关接口.py"])