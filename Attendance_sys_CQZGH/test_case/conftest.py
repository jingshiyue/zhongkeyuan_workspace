#!/usr/bin/python3
# Time : 2019/8/22 10:48 
# Author : zcl
import pytest
from WuLanChaBuApi.common.mysql_class import *
shujuku = DataBase("192.168.5.15", 3306, "root", "123456", "faceguard")
staff_tuple = shujuku.find_all('SELECT * FROM face_image WHERE face_image.`name` LIKE "测试考勤%" ;')

@pytest.fixture()
def staff_dic():
    staff = {}
    for i in staff_tuple:
        staff.setdefault(i[9],{})
        staff[i[9]].setdefault("num",i[0])
        staff[i[9]].setdefault("id",i[12])
    return staff