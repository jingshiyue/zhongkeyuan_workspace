# coding:utf-8
import pytest
from WuLanChaBuApi.common.mysql_class import DataBase
shujuku = DataBase("192.168.1.107", 3306, "root", "123456", "faceguard")


@pytest.fixture()
def add_dict_delete():
    shujuku.open_data_base()
    sql = "insert into base_dictory_value VALUES ('19','4','2018-09-19 15:10:56','2018-09-19 15:10:59','android','1');"
    shujuku.cud(sql)
    print("增加一条字典值")

    yield
    shujuku.open_data_base()
    sql1 = "delete FROM base_dictory_value WHERE id='19'"
    shujuku.cud(sql1)
    print("删除此数据记录")