#!/usr/bin/python3
# Time : 2019/8/22 10:48 
# Author : zcl
import pytest,sys
from WuLanChaBuApi.common.mysql_class import *
from Attendance_sys_CQZGH.utils.Log import mylog
logger = mylog.get_log().get_logger()
shujuku = DataBase("172.18.2.199", 3306, "root", "123456", "dynfacestore")
staff_tuple = shujuku.find_all('SELECT * FROM face_image WHERE face_image.`name` LIKE "测试20191217%" ;')  # %表示任意多个任意字符   _表示一个任意字符


@pytest.fixture()
def staff_dic():  #查询数据库，返回员工的信息，添加到字典里
    logger.info("打开数据库连接！！！")
    staff = {}
    for i in staff_tuple:
        staff.setdefault(i[9],{})
        staff[i[9]].setdefault("num",i[0])
        staff[i[9]].setdefault("id",i[12])
    yield staff
    shujuku.close_database()
    logger.info("断开数据库连接!!!")

