from Attendance_sys_CQZGH.utils.excel_operate import excel_obj
from Attendance_sys_CQZGH.utils.common_method import *
def f(reqId="a",personCode="b"):
    if data == "reqId":
        reqId = ""
    elif data == "personCode":
        personCode = ""

    print(reqId)
    print(personCode)


exl = excel_obj(sheet_name="3.9.2考勤登记相关接口接口",exl_f_path="D:\workfile\zhongkeyuan_workspace\Attendance_sys_CQZGH\重庆市总工会人脸识别考勤系统doc\重庆市总工会人脸识别考勤系统项目接口用例_20190815.xls")

d = read_case_title(exl,4,30)
print(d)