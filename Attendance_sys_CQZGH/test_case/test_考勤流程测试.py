#!/usr/bin/python3
# Time : 2019/8/22 13:45 
# Author : zcl
import pytest,sys,json
from WuLanChaBuApi.TestApi.test_Match_Record.MatchRecord import MatchRecord
from Attendance_sys_CQZGH.utils.common_method import *
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()
# from WuLanChaBuApi.TestApi.new_method import *
from WuLanChaBuApi.TestApi.Test_regist.Regist import Regist
from WuLanChaBuApi.TestApi.Test_facelib.FaceLib import FaceLib
from WuLanChaBuApi.common.mysql_class import *


shujuku = DataBase("192.168.5.15", 3306, "root", "123456", "faceguard")

###############################
#准备数据（制造考勤状态）：创建人脸数据库->创建底库 -> 绑定人脸库id与底库id
###############################
@pytest.mark.skip(reason="注册人脸信息,存在人脸信息表里")
def test_create_data_process_01():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    pic_path = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\100.jpg"
    _registInfo = [
        { "name":"正常考勤101",
         "sex":1,
         "personCode":"500382199001017022", #填身份证
         "cobDepartmentId":"4028858f6ccd13c0016ccd1a88a3000b",    #String    32位部门ID，对应3.3的部门表的ID
         "faceImg":to_base64(pic_path),
          "birthdayDate":"19900101",
          "nationality":"中国",
          "ethnic":"汉",
          "codeType":1
       }]
    body = {
         "reqId":get_uuid(),
         "num":1,
         "registInfo":_registInfo
    }
    res = Regist().api_v1_face_regist(body)
    logger.info(res.text)
    logger.info("人脸信息表里加入 人脸信息 完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


@pytest.mark.skip(reason="创建人脸底库")
def test_create_data_process_02():
    """创建人脸底库，数据放入face_library表"""
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    body = {"reqId": get_uuid(),
            "libraryName": "室内办公人员01",
            "libraryCode": "AA00101",
            "libraryType": 1,
            "remark": "在室内办公人员在这个底库"}
    res = FaceLib().api_v1_facelib_create(body)
    json_data = json.loads(res)
    logger.info(json_data)
    assert json.loads(res.text)["status"] == 0
    logger.info("创建底库 完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


@pytest.mark.skip(reason="人脸信息与人脸库的绑定接口，存在人脸图像库关系表里")
def test_create_data_process_03():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    relations = []
    """修改人脸信息与人脸库的绑定接口"""
    # yuanzu = shujuku.find_all("SELECT face_image.id FROM face_image;")
    # for i in range(0, 1002):
    #     relations_one = {"personId": yuanzu[i][0],
    #                      "faceLibIds": "402881e967a6e9200167a7044c4a514f",
    #                      "optType": 2,
    #                      "fId": get_uuid()}
    #     relations.append(relations_one)
    # relations = json.dumps(relations)

    relations_one = {"personId": "e1ebf165008a4aa385d2277618817d8d",  #人脸库id
                     "faceLibIds": "4028858f6cd61b18016cd63778fc0008", #底库id
                     "optType":0,  #0-新增，1-修改。2-删除
                     "fId": get_uuid()}
    relations.append(relations_one)
    relations = json.dumps(relations)

    body = {
        "reqId": get_uuid(),
        "relations": relations,
        "num": 1
    }
    res = Regist().api_v1_face_lib_binding(body)
    logger.info(res.text)
    assert json.loads(res.text)["status"] == 0
    logger.info("绑定人脸库id与底库id 完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)



###############################
#刷脸，登记考勤：同步刷脸 - >考勤流水查询 （前提:创建人脸数据库->创建底库 -> 绑定人脸库id与底库id）
###############################

@pytest.mark.skip(reason="产生刷脸数据，同步到考勤系统里")
def test_matchrecord_process_01():
    """
    产生刷脸数据
    :return:
    """
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    _MatchRecord = MatchRecord("http://192.168.5.15:10019/")
    picpath = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)"
    records = []
    # for time in ["20190822093000","20190822123000","20190822183000"]:  #一天的打卡时间
    for time in ["20190824090000","20190824120000"]:  # 一天的打卡时间
        for k in range(101, 102):
            record = {
                "id": get_uuid(),
                "baseDeviceCode": "Device1",
                "baseAreaCode": "T411",
                "faceImageId": "af04ab00fd0111e8bf04dca266365d7c",
                "personCode": "500382199001017022",
                "faceLibraryId": "402881e9679b7c6e01679b99647f0000",
                "areaName": "三级区域1",
                "faceName": "正常考勤%d" %k,
                "codeType": "0",
                "libraryName": "正常考勤",
                "swipeTime":time, #20190826083000,20190826123000,20190826183000     yyyyMMddHHmmss
                "livePhoto": to_base64(picpath + "\\" + "%d.jpg" % k),
                "threshold": "0.8",
                "matchingScore": "0.95555",
                "passStatus": "1",  #1，表示成功
                "personSex": "1",
                "noPassReason": ""
            }
            records.append(record)
        body = {
            "reqId": get_uuid(),
            "records": records,
            "num": len(records)
        }
        res = _MatchRecord.api_face_matchrecord_sync(body)
        logger.info(res.text)
        assert json.loads(res.text)["status"] == 0
        logger.info("%s 刷脸成功！！！" %time)
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="考勤流水查询，同步到考勤系统里")
def test_matchrecord_process_02():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_record_query(
        reqId=get_uuid(),  # 32位UUID	是
        name="正常考勤101",  # 员工名称	否
        deptId="",  # 部门ID，为空字符串，表示所有部门	是
        personCode="",  # 员工编码	否
        pageNum=1,  # 分页的起始页，从1开始	是
        pageSize=100,  # 分页的大小	是
        isCount=1,  # 为1表是返回总数	是
        startTime="20190822",  # yyyyMMdd	是
        endTime="20190829",  # yyyyMMdd	是
    )
    logger.info(res.text)
    assert json.loads(res.text)["status"] == 0
    logger.info("考勤流水记录查询完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


if __name__ == '__main__':
    pytest.main(["-q", "test_流程测试.py"])