# coding:utf-8
import pytest
from WuLanChaBuApi.common.mysql_class import DataBase
database = DataBase("192.168.1.107", 3306, "root", "123456", "faceguard")


@pytest.fixture()
def delete_facelib():
    yield
    database.open_data_base()
    sql1 = "select * FROM face_library WHERE library_code='AA001'"
    print("以下是新增底库成功后的结果\n")
    print(database.find_all(sql1))
    sql = "delete FROM face_library WHERE library_code='AA001';"
    database.cud(sql)
    print("新增后后置处理=====数据删除")


@pytest.fixture()
def query_update():
    database.open_data_base()
    sq2 = "select * FROM face-library WHERE library_code='code001'"
    print("以下是更新之前的数据\n")
    print(database.find_all(sq2))
    yield
    database.open_data_base()
    sql1 = "select * FROM face_library WHERE library_code='code001'"
    print("以下是成功更新底库后的结果\n")
    print(database.find_all(sql1))
    sql = "delete FROM face_library WHERE library_code='code001';"
    database.cud(sql)
    print("新增后后置处理=====数据删除")
