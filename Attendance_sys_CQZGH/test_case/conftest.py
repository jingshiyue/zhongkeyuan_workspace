#!/usr/bin/python3
# Time : 2019/8/22 10:48 
# Author : zcl
import pytest,sys
sys.path.append(r"D:\workfile\zhongkeyuan_workspace")
from WuLanChaBuApi.common.mysql_class import *
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()
shujuku = DataBase("192.168.5.15", 3306, "root", "123456", "faceguard")
staff_tuple = shujuku.find_all('SELECT * FROM face_image WHERE face_image.`name` LIKE "测试考勤%" ;')

@pytest.fixture()
def staff_dic():
    logger.info("打开数据库连接！！！")
    staff = {}
    for i in staff_tuple:
        staff.setdefault(i[9],{})
        staff[i[9]].setdefault("num",i[0])
        staff[i[9]].setdefault("id",i[12])
    yield staff
    shujuku.close_database()
    logger.info("断开数据库连接!!!")