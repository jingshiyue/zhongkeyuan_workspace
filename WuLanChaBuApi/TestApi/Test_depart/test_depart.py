# coding:utf-8
import pytest
from WuLanChaBuApi.TestApi.new_method import *
from WuLanChaBuApi.TestApi.Test_depart.Depart import Depart
import json
depart = Depart()

@pytest.mark.skip(reason="不作为正常测试")
def test_save_01(delete_depart):
    """能正确新增部门信息"""
    body = {"reqId": get_uuid(),      # 32位UUID
            "departmentCode": "testA001",  # 部门编号
            "departmentName": "部门名称",  # 部门名称
            "createdTime": "2018-11-27 11:43:41",
            "address": "北京市海淀区",
            "linkman": "陈克云",
            "linkPhone": "18680946659",
            "headUserId": "aa11f12ed5cf4eedaa8a9b470bcc0252",
            "level": 1,    # 必填
            "parentDepartmentId": 0,
            "createdUserId": "e0f9afe9804b4eac89d52a428ea3e236",
            "note": "二级学院"
            }
    res = depart.api_system_department_save(body)
    json_data = json.loads(res)
    assert json_data["status"] == 0



@pytest.mark.skip(reason="")
def test_save_test_test():
    body = {"reqId": get_uuid(),      # 32位UUID
            "departmentCode": "SMscience111",  # 部门编号
            "departmentName": "生物与化学环境科学111",  # 部门名称
            # "createdTime": "2018-11-27 11:43:41",
            "address": "北京市海淀区",
            "linkman": "陈克云",
            "linkPhone": "18680946659",
            "headUserId": "aa11f12ed5cf4eedaa8a9b470bcc0252",
            "level": 3,    # 必填
            "parentDepartmentId": "402881e96796dd41016796ef6e680027",
            "createdUserId": "e0f9afe9804b4eac89d52a428ea3e236",
            "note": "二级学院"
            }
    res = depart.api_system_department_save(body)


@pytest.mark.skip(reason="仅作为异常测试，不作为正常测试")
def test_save_02():
    """重复增加部门信息"""
    body = {"reqId": get_uuid(),      # 32位UUID
            "departmentCode": "SMscience",  # 部门编号
            "departmentName": "生物与化学环境科学",  # 部门名称
            "address": None,
            "linkman": None,
            "linkPhone": "110",
            "headUserId": "001",
            "level": 1,    # 必填
            "parentDepartmentId": "4028806a674f79d5016753da6aac002d",
            "createdUserId": "test001",
            "note": "fuji区域"
            }
    res = depart.api_system_department_save(body)
    json_data = json.loads(res)
    assert json_data["msg"] == "value repeat insert:departmentCode"

@pytest.mark.skip(reason="不作为正常测试")
def test_update_01():
    """部门信息更新"""
    body = {"reqId": get_uuid(),      # 32位UUID
            "departmentId": "402881e96796dd41016796f579690028",
            "departmentCode": "SMscience",  # 部门编号
            "departmentName": "生物与化学环境科学",  # 部门名称
            "address": "北京市海淀区",
            "linkman": "陈克云",
            "linkPhone": "18680946659",
            "headUserId": "402881e96796dd41016796ef6e680027",
            "level": 3,    # 必填
            "parentDepartmentId": "402881e96796dd41016796ef6e680027",
            "createdUserId": "e0f9afe9804b4eac89d52a428ea3e236",
            "note": "三级学院-专业"
            }
    res = depart.api_system_department_update(body)

@pytest.mark.skip(reason="不作为正常测试")
def test_delete_01():
    """验证部门信息删除"""
    body = {"reqId": get_uuid(),
            "ids": "402881e96796dd41016796fe768c002c,jjj"}
    depart.api_system_department_delete(body)

@pytest.mark.skip(reason="")
def test_query_01():
    """验证能查询出部门信息"""
    body = {"reqId": get_uuid()}
    res = depart.api_system_department_query(body)
    json_data = json.loads(res)
    print(len(json_data["results"]))
    for i in range(0, len(json_data["results"])):
        print(json_data["results"][i])

# @pytest.mark.skip(reason="")
def test_detail_01():
    """验证能正确查询出部门的详细信息"""
    body = {"reqId": get_uuid(),
            "departmentId": "4028858f6ccd13c0016ccd1a88a3000b",
            "isCount": 1,
            "pageNum": 1,
            "pageSize": 1}
    res = depart.api_system_department_detail(body)


if __name__ == '__main__':
    pytest.main(["-q", "test_depart.py"])
