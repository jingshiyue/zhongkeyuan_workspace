# coding:utf-8
import hashlib
import base64
import time
import uuid
from datetime import datetime
from _datetime import timedelta
import random
import os
import linecache
import json
import requests
import logging
id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
# handler = logging.FileHandler("log.log", encoding="utf-8")
# handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)

# logger.addHandler(handler)
logger.addHandler(console)


def to_md5_str(str_code):
    """
    将字符串转换成md5加密字符串
    :param str_code: 待加密的对象
    :return:
    """
    m = hashlib.md5()
    m.update(str_code.encode(encoding="utf-8"))
    str_encoding = m.hexdigest()
    return str_encoding


def to_base64(picturepath):
    """
    将图片转换成base64编码
    :param picturepath:图片文件路径
    :return:
    """
    with open(picturepath, mode="rb") as fp:
        imaga_data = fp.read()
        base64_data = base64.b64encode(imaga_data)
        return str(base64_data, encoding="utf-8")


def get_time_stamp():
    """
    返回毫秒级的时间戳
    :return:
    """
    return str(round(time.time()*1000))


def delete_str(str1):
    """
    删除字符-
    :param str1:
    :return:
    """
    strr = str1.split("-")
    output = ''
    for b in range(len(strr)):
        output += strr[b]
    return output


def get_uuid():
    """
    获取32位uuid字符串
    :return:
    """
    m = str(uuid.uuid1())
    return delete_str(m)


def get_time_mmss():
    """
    返回YYYYMMDDhhmmss的时间格式
    :return:
    """
    return str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))


def get_time_month_ago():
    """
    获取当前时间和一个月以前的时间
    :return:
    """
    next_time = (datetime.now() - timedelta(days=20)).strftime("%Y%m%d%H%M%S")
    return str(next_time)


def produce_flight_date():
    """
    以当前时间，生成航班日期
    :return:
    """
    flight_date_old = get_time_mmss()
    flight_date = flight_date_old[0:8]
    return str(flight_date)


def get_flight_out_time(h=3):
    """
    在当前时间上加上对应的延迟时间作为起飞时间
    :param h: 需要延迟的时间
    :return:
    """
    next_time = (datetime.now() + timedelta(hours=h)).strftime("%Y%m%d%H%M%S")
    return str(next_time)


def get_zhiji(h=1):
    """以延迟当前时间作为值机日期获取值机日期"""
    next_time = (datetime.now() - timedelta(hours=h)).strftime("%Y%m%d%H%M%S")
    return str(next_time)



def get_age(id_number):
    """通过身份证号获取年龄"""
    current = int(time.strftime("%Y"))
    year = int(id_number[6:10])
    age = current-year
    return age


def get_bir_year(id_number):
    """
    获取旅客的出生年
    :param id_number:
    :return:
    """
    year = int(id_number[6:10])
    return year


def get_birthday(id_number):
    """
    通过身份证号码获取生日日期
    :param id_number:
    :return:
    """
    birthday_date = id_number[6:14]
    return str(birthday_date)


def get_lk_bdno():
    """
    生成三位随机的登机序列号
    :return:
    """
    lk_bdno = random.randint(100, 999)
    return str(lk_bdno)


def get_lk_desk():
    """
    生成随机的机场目的地
    :return:
    """
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, "aj系统xml文件")
    list_desk = linecache.getlines(file_path+"/"+"air.txt")
    return str(list_desk[random.randint(0, 154)]).rstrip("\n")


def get_add_idcard(card,p=0,l=18):
    """
    讲当前的数字生成规定位数的数字，:param card: 号码:param p: 替补的数字:param l: 一共需要的位数
    :param card: 号码
    :param p: 替补的数字
    :param l: 一共需要的位数
    :return:
    """
    m = str(0)
    if (len(str(card)) < l):
        for k in range(0,l-len(str(card))-1):
                m = m + str(p)
    else:
        raise Exception
    return m+str(card)


def get_txt(txtpath):
    with open(txtpath, "r") as fp:
        data = fp.read().rstrip()
    return str(data)


def get_features(filepath:str, mode="8K") ->str:
    global json_data
    body = {"FileName": filepath}
    header = {"Content-type": "application/json"}
    res = requests.post(url="http://127.0.0.1:7081/feature/v1/request",
                        headers=header,
                        json=body,
                        verify=False)
    try:
        json_data = json.loads(res.text)
        if mode.__eq__("8K"):
            feature = json_data["Feature8K"]
        else:
            feature = json_data["Feature2K"]
        logger.info(feature)
        return feature
    except:
        logger.warning("质量不好，提取失败")


if __name__ == '__main__':
    # print(get_uuid())
    print(to_md5_str("nidexuanze"))
    print(get_time_stamp())
    print(get_time_mmss())
    # print(get_features("C:\\chenkeyun\\Tools\shoudu\\chenkeyunli_gaitubao_com_1280x720.JPG", mode="2K"))
    print(to_base64("C:\\Users\\Original Dream\\Desktop\\$[00}1TBGW57F@GF2HPG$R5.jpg").__len__())


    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;".__len__())
