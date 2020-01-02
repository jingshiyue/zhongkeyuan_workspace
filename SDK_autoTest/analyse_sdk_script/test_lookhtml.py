#!/usr/bin/python3
# Time : 2019/8/29 15:03 
# Author : zcl
import pytest
import json,sys,logging

# log_path = "Monitor_CPU_RAM_%s.txt" % time.strftime('%Y%m%d%H%M%S',time.localtime())
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # filename = log_path,
    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
console.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console)


# @pytest.mark.skip(reason="考勤导出")
def test_attendence_record_export():
    logging.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="考勤流水-导出下载")
def test_attendence_record_download():
    logging.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)



if __name__ == '__main__':
    pytest.main(["-s", "test_lookhtml.py"])
