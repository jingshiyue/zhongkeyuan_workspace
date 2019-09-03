#!/usr/bin/python3
# Time : 2019/9/2 11:51 
# Author : zcl
import pytest,sys,json
from WuLanChaBuApi.TestApi.test_Match_Record.MatchRecord import MatchRecord
from Attendance_sys_CQZGH.utils.common_method import *
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *
# from WuLanChaBuApi.TestApi.new_method import *
from WuLanChaBuApi.TestApi.Test_regist.Regist import Regist
from WuLanChaBuApi.TestApi.Test_facelib.FaceLib import FaceLib
from WuLanChaBuApi.TestApi.Test_depart.Depart import Depart
from WuLanChaBuApi.common.mysql_class import *
import threading
import time as Time


def face_matchrecord_sync(staff_dic,staff_num=10):
    _MatchRecord = MatchRecord("http://192.168.5.15:10019/")
    picpath = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)"
    records = []
    k = 100
    m = 0
    for staff, value in staff_dic.items():
        if m < staff_num:
            for time in ["20190901090000"]:  # 一天的打卡时间
                # for time in ["20190830120000"]:  # 一天的打卡时间
                record = {
                    "id": get_uuid(),
                    "baseDeviceCode": "Device1",
                    "baseAreaCode": "T411",
                    "faceImageId": staff_dic[staff]["num"],
                    "personCode": staff_dic[staff]["id"],
                    "faceLibraryId": "4028858f6cd61b18016cd65d511c010b",
                    "areaName": "三级区域1",
                    "faceName": staff,
                    "codeType": "0",
                    "libraryName": "测试考勤",
                    "swipeTime": time,  # 20190826083000,20190826123000,20190826183000     yyyyMMddHHmmss
                    "livePhoto": to_base64(picpath + "\\" + "%d.jpg" % k),
                    "threshold": "0.8",
                    "matchingScore": "0.95555",
                    "passStatus": "1",  # 1，表示成功
                    "personSex": "1",
                    "noPassReason": ""
                }
                records.append(record)
            k += 1
            m += 1
    body = {
        "reqId": get_uuid(),
        "records": records,
        "num": len(records)
    }
    start_time = Time.clock()
    start_time1 = Time.time()
    res = _MatchRecord.api_face_matchrecord_sync(body)
    logger.info(res.text)
    assert json.loads(res.text)["status"] == 0
    end_time = Time.clock()
    end_time1 = Time.time()
    logger.info("响应时间：" + str(end_time-start_time))
    logger.info("walktime:" +str(end_time1-start_time1))



def test_face_matchrecord_sync(staff_dic,staff_num=30):
    """
    :param:刷脸的员工人数，最大不能超过注册的员工数量
    :return:
    """
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    thread_list = []
    while True:
        t_start = Time.time()
        for i in range(10):
            t = threading.Thread(target=face_matchrecord_sync,args=[staff_dic,staff_num])
            thread_list.append(t)
        for j in thread_list:
            j.start()
            logger.info("线程：" + j.getName() + "  START...")
        t_end = Time.time()
        thread_list = []
        logger.info("完成一轮，下一轮间隔5min。本轮用时%s" %(t_end-t_start))
        Time.sleep(60*5)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)

if __name__ == '__main__':
    pytest.main(["-q", "刷脸同步接口性能测试.py"])