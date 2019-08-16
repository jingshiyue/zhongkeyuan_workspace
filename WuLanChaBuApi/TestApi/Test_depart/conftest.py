# coding:utf-8
import pytest
from WuLanChaBuApi.common.mysql_class import DataBase
shujuku = DataBase("192.168.1.107", 3306, "root", "123456", "faceguard")


@pytest.fixture()
def delete_depart():
    yield
    shujuku.open_data_base()
    sql2 = 'select * FROM face_department WHERE department_code="testA001";'
    print("以下是数据库中新增成功的部门信息")
    print(shujuku.find_all(sql2))
    sql = "delete FROM face_department WHERE department_code='testA001';"
    shujuku.cud(sql)
    print("新增后删除成功")