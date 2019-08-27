# coding:utf-8
import pytest
from WuLanChaBuApi.TestApi.test_Match_Record.MatchRecord import *
current_path = os.path.realpath(__file__)
dirpath = os.path.dirname(current_path)
dirpath = os.path.dirname(dirpath)
dirpath = os.path.dirname(dirpath)
picpath = os.path.join(dirpath, "common\\picture")
picpath = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)"

def test_match_record(i=100,j= 110):
    """"""
    records = []
    for k in range(i, j):
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
            "livePhoto": to_base64(picpath+"\\"+"%d.jpg" % k),
            "threshold": "0.8",
            "matchingScore": "0.9",
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
    MatchRecord().api_face_matchrecord_sync(body)

if __name__ == '__main__':
    pytest.main(["-q", "test_match_record.py"])