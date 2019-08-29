# coding:utf-8
import pytest
from WuLanChaBuApi.TestApi.test_Match_Record.MatchRecord import *
current_path = os.path.realpath(__file__)
dirpath = os.path.dirname(current_path)
dirpath = os.path.dirname(dirpath)
dirpath = os.path.dirname(dirpath)
picpath = os.path.join(dirpath, "common\\picture")
picpath = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)"


def match_record(i=100,j= 101):
    """"""
    records = []
    for k in range(i, j):
        record = {
            "id": get_uuid(),
            "baseDeviceCode": "Device1",
            "baseAreaCode": "T411",
            "faceImageId": "e1ebf165008a4aa385d2277618817d8d",
            "personCode": "500382199001017022",
            "faceLibraryId": "4028858f6cd61b18016cd65d511c010b",
            "areaName": "三级区域1",
            "faceName": "正常考勤101",
            "codeType": "0",
            "libraryName": "室内办公人员01",
            "swipeTime": "2019082708080000",
            "livePhoto": to_base64(picpath+"\\"+"%d.jpg" % k),
            "threshold": "0.8",
            "matchingScore": "0.9",
            "passStatus": "1",
            "personSex": "1",
            "noPassReason": ""
        }
        records.append(record)
    body = {
        "reqId": get_uuid(),
        "records": records,
        "num": len(records)
    }
    res = MatchRecord().api_face_matchrecord_sync(body)
    print(res.text)

match_record()


# if __name__ == '__main__':
#     pytest.main(["-q", "test_match_record.py"])