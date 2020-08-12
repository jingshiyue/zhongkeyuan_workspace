#!/usr/bin/python3
# Time : 2019/8/22 13:45 
# Author : zcl
import pytest,sys,json
from WuLanChaBuApi.TestApi.test_Match_Record.MatchRecord import MatchRecord
from Attendance_sys_CQZGH.utils.common_method import *
from Attendance_sys_CQZGH.Attendance_sys_CQZGH_api import *
logger = mylog.get_log().get_logger()
from WuLanChaBuApi.TestApi.new_method import *
from WuLanChaBuApi.TestApi.Test_regist.Regist import Regist
from WuLanChaBuApi.TestApi.Test_facelib.FaceLib import FaceLib
from WuLanChaBuApi.TestApi.Test_depart.Depart import Depart
from WuLanChaBuApi.common.mysql_class import *


depart = Depart(host="http://172.18.2.199:9091/face-bussiness-server/")
###############################
#准备数据（制造考勤状态）：创建部门-> 创建底库 -> 创建人脸数据库->绑定人脸库id与底库id
###############################
@pytest.mark.skip(reason="创建部门,当没有部门时，需先创建部门,有1级部门，2级部门等")
def test_create_data_process_01():
    """能正确新增部门信息"""
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    body = {"reqId": get_uuid(),      # 32位UUID
            "departmentCode": get_uuid(),  # 部门编号
            "departmentName": "新增部门02",  # 部门名称
            "createdTime": "2019-12-17 11:49:41",
            "address": "重庆",
            "linkman": "xx",
            "linkPhone": "18680946659",
            "headUserId": "",
            "level": 1,    # 必填
            "parentDepartmentId": 0,
            "createdUserId": "e1ebf165008a4aa385d2277618817d8d",
            "note": "二级学院"
            }
    res = depart.api_system_department_save(body)
    assert json.loads(res.text)["status"] == 0
    logger.info("创建部门 完成！！！")
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
    res = FaceLib("http://175.168.1.128:9091/face-bussiness-server/").api_v1_facelib_create(body)
    json_data = json.loads(res.text)
    logger.info(json_data)
    # assert json.loads(res.text)["status"] == 0
    logger.info("创建底库 完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="注册人脸信息,存在人脸信息表里")
def test_create_data_process_03(start=140,end=160):#添加人数
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    _registInfo = []
    for num in range(start,end):
        reg_info = { "name":"测试20191217%d" %num,
                     "sex":1,
                     "personCode":"501382199201017%d" %num, #填身份证
                     "cobDepartmentId":"2f2881006efe13c1016f11a4f4350004",    #String    32位部门ID，对应3.3的部门表的ID
                     "faceImg":to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\%d.jpg" %num),
                     "birthdayDate":"19920101",
                      "nationality":"小日本鬼子",
                      "ethnic":"汉",
                      "codeType":1,
                      "entryDate":"20190925"    #非必须    yyyyMMdd  
                     }
        _registInfo.append(reg_info)
    body = {
         "reqId":get_uuid(),
         "num":len(_registInfo),
         "registInfo":_registInfo,
    }

    res = Regist(host="http://175.168.1.128:10020/").api_v1_face_regist(body)
    logger.info(res.text)
    logger.info("人脸信息表里加入 人脸信息 完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="人脸信息与人脸库的绑定接口，存在人脸图像库关系表里")
def test_create_data_process_04(staff_dic):
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    relations = []
    """修改人脸信息与人脸库的绑定接口"""
    for i in staff_dic:
        print(staff_dic[i]["num"])
        relations_one = {"personId": staff_dic[i]["id"],
                         "faceLibIds": "2f2881006efe13c1016f11a4f4350004", #底库id
                         "optType": 2,
                         "fId": get_uuid()}
        relations.append(relations_one)
    relations = json.dumps(relations)

    body = {
        "reqId": get_uuid(),
        "relations": relations,
        "num": len(staff_dic)
    }
    res = Regist().api_v1_face_lib_binding(body)
    logger.info(res.text)
    assert json.loads(res.text)["status"] == 0
    logger.info("绑定人脸库id与底库id 完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)



###############################
#刷脸，登记考勤：同步刷脸 - >考勤流水查询 （前提:创建人脸数据库->创建底库 -> 绑定人脸库id与底库id）
###############################
# @pytest.mark.skip(reason="刷脸，同步到考勤系统里")
def test_matchrecord_process_01(staff_dic,staff_num=35):
    """
    :param:刷脸的员工人数，最大不能超过注册的员工数量
    :return:
    """
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    _MatchRecord = MatchRecord("http://172.18.2.199:10019/")
    picpath = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)"
    records = []
    k = 100
    m = 0
    for staff, value in staff_dic.items():
        if m < staff_num:
            for time in ["20190923093000","20190923123000","20190923183000"]:  #一天的打卡时间
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
                    "swipeTime":time, #20190826083000,20190826123000,20190826183000     yyyyMMddHHmmss
                    "livePhoto": to_base64(picpath + "\\" + "%d.jpg" % k),
                    "threshold": "0.8",
                    "matchingScore": "0.95555",
                    "passStatus": "1",  #1，表示成功
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
    res = _MatchRecord.api_face_matchrecord_sync(body)
    logger.info(res.text)
    # assert json.loads(res.text)["status"] == 0
    logger.info("刷脸成功！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="考勤流水查询，同步到考勤系统里")
def test_matchrecord_process_02():
    logger.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = attendance_sys().api_v1_attendence_record_query(
        reqId=get_uuid(),  # 32位UUID	是
        name="测试考勤101",  # 员工名称	否
        deptId="",  # 部门ID，为空字符串，表示所有部门	是
        personCode="",  # 员工编码	否
        pageNum=1,  # 分页的起始页，从1开始	是
        pageSize=100,  # 分页的大小	是
        isCount=1,  # 为1表是返回总数	是
        startTime="20190901",  # yyyyMMdd	是
        endTime="20190901",  # yyyyMMdd	是
    )
    logger.info(res.text)
    assert json.loads(res.text)["status"] == 0
    logger.info("考勤流水记录查询完成！！！")
    logger.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


if __name__ == '__main__':
    pytest.main(["-s", "test_流程测试.py"])