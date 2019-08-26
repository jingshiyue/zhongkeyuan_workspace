#!/usr/bin/python3
# Time : 2019/8/22 13:45 
# Author : zcl
# import pytest
from WuLanChaBuApi.TestApi.test_Match_Record.MatchRecord import MatchRecord
from Attendance_sys_CQZGH.utils.common_method import *
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()


def add_matchrecord():
    """
    产生刷脸数据
    :return:
    """
    _MatchRecord = MatchRecord("http://192.168.5.15:10010/")
    picpath = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)"
    records = []
    for k in range(100, 110):
        record = {
            "id": get_uuid(),
            "baseDeviceCode": "Device1",
            "baseAreaCode": "T411",
            "faceImageId": "af04ab00fd0111e8bf04dca266365d7c",
            "personCode": "寅时三刻发贱鬼2",
            "faceLibraryId": "402881e9679b7c6e01679b99647f0000",
            "areaName": "三级区域1",
            "faceName": "寅时三刻发贱鬼2",
            "codeType": "0",
            "libraryName": "寅时三刻发贱鬼",
            "swipeTime": "2048030608080000",
            "livePhoto": to_base64(picpath + "\\" + "%d.jpg" % k),
            "threshold": "0.8",
            "matchingScore": "0.000111112121545454",
            "passStatus": "0",
            "personSex": "1",
            "noPassReason": ""
        }
        records.append(record)
    body = {
        "reqId": get_uuid(),
        "records": records,
        "num": len(records)
    }
    _MatchRecord.api_face_matchrecord_sync(body)

add_matchrecord()
# if __name__ == '__main__':
#     pytest.main(["-q", "test_流程测试.py"])