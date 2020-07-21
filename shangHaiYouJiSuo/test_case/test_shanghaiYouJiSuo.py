#!/usr/bin/python3
# Time : 2019/12/6 10:02
# Author : zcl
import pytest,random,os,sys,pymysql
from dongTaiBuKong.DTBK_api import dongTaiBuKong
from dongTaiBuKong.utils.common_method import *
from dongTaiBuKong.utils.logging import *
from WuLanChaBuApi.TestApi.Test_regist.Regist import *

def printRes(res):
    logging.info("------------------------------------------------")
    logging.info(res.text)
    logging.info("------------------------------------------------")

# def log_fuc(func):
#     def wrapper(*args, **kw):
#         logging.info("------------------------------------------------")
#         func(*args, **kw):
#         logging.info("------------------------------------------------")
#     return wrapper


# @pytest.mark.skip(reason="测试摄像头绑定接口，增加与删除")
def test_01():
    res = dongTaiBuKong().api_v1_system_device_camera_binding(
        reqId=get_uuid(),  # 必须
        cameraDeviceCode="SXTBM12",  # 必须 摄像头编码逗号隔开
        captureDeviceCode="ZPFWQ1",  # 必须 抓拍服务器编码
        optType=2  # 必须 integer 0-添加；2-删除
    )
    printRes(res)


# @pytest.mark.skip(reason="摄像头查询接口")
def test_02():
    res = dongTaiBuKong().api_v1_system_device_binding_query(
        reqId=get_uuid(),  # 必须
        captureDeviceCode="",  # 非必须
        isCount=1,  # 必须
        pageSize=10,  # integer 必须
        pageNum=1,  # integer 必须
    )
    printRes(res)


@pytest.mark.skip(reason="抓拍服务器注册")
def test_03():
    res = dongTaiBuKong().api_v1_client_regist(
        reqId=get_uuid(),  # 必须
        deviceCode="zhuapai1",  # 必须
        areaCode="T111",  # 必须
    )
    printRes(res)

# @pytest.mark.skip(reason="人脸识别接口...[人脸信息注册在考勤项目里]")
def test_04():
    pic_path = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\1.jpg"
    txt_path = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture2k\1.txt"
    _imageInfo = [{"faceImg":to_base64(pic_path),
                  "faceFeature":read_feature(txt_path),
                  "fId":"123213",
                  "qualityScore":19
                   }]
    """人脸识别接口"""
    res = dongTaiBuKong().api_v1_face_review_check(
        reqId=get_uuid(),
        areaCode="T111",
        deviceCode="zhuapai1",
        deviceType=0,
        deviceName="抓拍服务器1",
        captureCode="zhuapai1",
        imageInfo=_imageInfo,
    )
    printRes(res)


# @pytest.mark.skip(reason="以图搜图接口，查询的是face_swipe_record表")
def test_05():
    pic_path = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\144.jpg"
    res = dongTaiBuKong().api_v1_face_record_imgsearch(
        reqId=get_uuid(),  # 必须
        img=to_base64(pic_path),  # 必须 64位base图片
        startDate="20191217",  # 必须
        endDate="20191219",  # 必须
        pageNum=1,  # 必须integer
        pageSize=10,  # 必须integer
        isCount=1,  # 必须integer 为1-返回总数
    )
    printRes(res)

# @pytest.mark.skip(reason="人脸识别记录-详情")
def test_06():
    res = dongTaiBuKong().api_v1_face_record_search_details(
        reqId=get_uuid(),  # 必须
        id="d45f9e114d4243b690729f43f4a34fda" ,# 必须
    )
    printRes(res)

# @pytest.mark.skip(reason="人脸识别记录-列表-条件查询")
def test_07():
    res = dongTaiBuKong().api_v1_face_record_search_list(
        reqId=get_uuid(),  # 必须
        pageSize=10,  # 必须
        pageIndex=1,# 必须
        isStranger=1,
    )
    printRes(res)


if __name__ == '__main__':
    pytest.main(["-q", "test_shanghaiYouJiSuo.py.py"])



