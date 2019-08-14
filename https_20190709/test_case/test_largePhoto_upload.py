#!/usr/bin/python3
# Time : 2019/8/13 9:15 
# Author : zcl
import pytest,random,os,sys,pymysql
from https_20190709.common.common_method import *
from https_20190709.common.params_init_z import *
from BaiTaAirport2_month.common import Idcardnumber
from https_20190709.API_https.AirportProcess import *
from https_20190709.common.Log_z import mylog
from BaiTaAirport2_month.msgQueue import Autosendlk
from BaiTaAirport2_month.common.mysql_class import *
logger = mylog.get_log().get_logger()


@pytest.fixture()
def struct_pho():
    """
    初始化照片、特征
    :return:
    """
    pho_dic = {}
    scenePhoto = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\2.jpg")
    cardPhoto = scenePhoto
    largePhoto = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\0.jpg")

    feature_files = os.listdir(r"D:\workfile\zhongkeyuan_workspace\test_photoes\idcard8k")
    feature_file = feature_files[random.randint(0, len(feature_files) - 1)]
    sceneFeature = read_feature(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture8k",feature_file))
    sceneFeature_2k = read_feature(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture2k",feature_file))
    cardFeature = read_feature(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\idcard8k",feature_file))

    pho_dic["scenePhoto"] = scenePhoto
    pho_dic["cardPhoto"] = cardPhoto
    pho_dic["largePhoto"] = largePhoto
    pho_dic["cardFeature"] = cardFeature
    pho_dic["sceneFeature"] = sceneFeature
    pho_dic["sceneFeature_2k"] = sceneFeature_2k
    return pho_dic


@pytest.fixture()
def insert_data_into_mysql(host="175.168.1.91",
                           port="3306",
                           user="root",
                           password="123456",
                           db="secsystem",
                           charset="utf8mb4",
                           sql=""
                           ):
    try:
        # Connect to the database
        connection = pymysql.connect(host=host,
                                     port=int(port),
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset=charset,
                                     cursorclass=pymysql.cursors.DictCursor)
    except pymysql.err.OperationalError as e:
        logger.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    bdno = str(random.randint(1,999))
    date = produce_flight_date()
    flight_no = produce_flight_number()
    sql = "insert into sec_passenger_entity(bdno,date,flight,strt) values ('%s','%s','%s','het');" % (
    bdno, date, flight_no)
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            connection.commit()
            logger.info("表:sec_passenger_entity 插入数据成功")
        except:
            connection.rollback()
            logger.error("表:sec_passenger_entity 插入数据失败...")
            exit()
    return bdno,date,flight_no


@pytest.fixture()
def creat_zhiji_random(insert_data_into_mysql):
    """
    在值机前先往表里（sec_passenger_entity）加入数据
    产生随机的值机人信息（起飞时间不管，主要是航班号，序号，身份证号码），信息在lkxx1.xml里
    """
    zhiji_dic = {}
    sex = random.randint(1, 2)
    idNo = Idcardnumber.get_random_id_number(sex=sex)
    lk_chkt = get_time_mmss()
    lk_flight = insert_data_into_mysql[2]
    lk_bdno = insert_data_into_mysql[0]
    lk_date = produce_flight_date()
    lk_id = str(random.randint(1, 999))
    lk_outtime = get_flight_out_time()
    Autosendlk.send_lkxx(
        lk_IsInternation="0",  # 1     是否国际 0否，1是，2未知
        lk_bdno=lk_bdno,  # 2     <!--2 10 登机序号 -->  3位
        lk_cardid=idNo,  # 4     证件号码
        lk_chkt=lk_chkt,  # 6     值机日期
        lk_cname="西瓜",  # 8     旅客中文姓名80
        lk_date=lk_date,  # 9     9航班日期 8 YYYYMMDD
        lk_del="0",  # 10    是否删除 0否  1是
        lk_desk="CTU",  # 11    11目的地  机场三字代表码
        lk_ename="XIGUA",  # 12    旅客英文姓名
        lk_flight=lk_flight,  # 13    航班号 12
        lk_gateno="10",  # 14    登机口号码 无意义k_g
        lk_id=lk_id,  # 15    旅客ID 主键 str 36
        lk_inf=" ",  # 16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
        lk_insur="0",  # 18    是否购保1
        lk_outtime=lk_outtime,  # 20    旅客起飞时间
        lk_sex=str(sex),  # 23    性别  1男性 2女性 0 未知
        lk_vip="0")
    zhiji_dic["idNo"] = idNo #身份证号
    zhiji_dic["lk_flight"] = lk_flight #航班号
    zhiji_dic["lk_bdno"] = lk_bdno #登机序号
    zhiji_dic["lk_date"] = lk_date #航班日期 8 YYYYMMDD
    zhiji_dic["lk_chkt"] = lk_chkt #值机日期 返回YYYYMMDDhhmmss的时间格式
    # zhiji_dic[""] =
    # zhiji_dic[""] =
    # zhiji_dic[""] =
    # zhiji_dic[""] =
    logger.info(zhiji_dic)
    return zhiji_dic

def log(res):
    """
    打印结果
    :param res:
    :return:
    """
    logger.info("---------------------------------------------------")
    logger.info(res.text)
    logger.info("---------------------------------------------------")
    sleep(1)





#######################################################################################
# @pytest.mark.skip(reason="debug skip")
def test_02(creat_zhiji_random,struct_pho): #02表示第二行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填,A B门T1AJ1，复核对应T1AF1
        deviceId="T1AJ001",  # 必填
        cardType="0",  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
        age=get_age(zhiji_dic["idNo"]),
        sex=1,
        birthDate=get_birthday(zhiji_dic["idNo"]),  # 必填
        address="重庆市",
        certificateValidity="20120101-20230202",  # 必填
        nationality="CHina",
        ethnic="汉族",
        contactWay="13512134390",
        cardPhoto=pho_dic["cardPhoto"],  # 必填
        fId=get_uuid()  # 必填
    )
    log(res)
    """2.3.21自助验证闸机B门接口（二期）"""

    res = AirportProcess().api_face_security_face_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填
        deviceId="T1AJ001",  # 必填
        cardType=0,  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
        age=get_age(zhiji_dic["idNo"]),
        sex="1",
        birthDate=get_birthday(zhiji_dic["idNo"]),  # 必填
        address="重庆市",
        certificateValidity="20180101-20260203",  # 必填
        nationality="China",  # 必填
        ethnic="汉族",  # 必填
        contactWay="13512134390",
        scenePhoto=pho_dic["scenePhoto"],  # 必填
        sceneFeature=pho_dic["sceneFeature"],  # 必填
        cardPhoto=pho_dic["cardPhoto"],  # 必填
        cardFeature=pho_dic["cardFeature"],  # 必填
        largePhoto=pho_dic["largePhoto"]  # 必填
    )
    log(res)

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)

    """2.3.24	人员回查-安检、登机口接口（二期）"""
    res = AirportProcess().api_face_data_flowback_query(
        reqId=get_uuid(),
        cardId=zhiji_dic["idNo"],
        flightNo=zhiji_dic["lk_flight"],
        flightDay=zhiji_dic["lk_date"],  # 航班dd
        boardingNumber=zhiji_dic["lk_bdno"],
        isFuzzyQuery=0)  # 不传是默认模糊查询，传值1-为模糊查询，非1为精确查询
    log(res)

    logger.info("test_02测试完成")

@pytest.mark.skip(reason="debug skip")
def test_03(creat_zhiji_random,struct_pho): #03表示第三行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=0,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
                        reqId=get_uuid(),
                        gateNo="T1AF1",
                        deviceId="T1AF002",
                        scenePhoto=pho_dic["scenePhoto"],
                        cardNo=zhiji_dic["idNo"],
                        passengerName="西瓜",
                        passengerEnglishName="xigua",
                        securityStatus=1,#安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
                        securityPassTime=zhiji_dic["lk_chkt"],
                        securityGateNo="",
                        securityDeviceNo="",
                        flightNo=zhiji_dic["lk_flight"],
                        boardingNumber=zhiji_dic["lk_bdno"],
                        sourceType=0,
                        flightDay=zhiji_dic["lk_date"])
    log(res)
    logger.info("test_03测试完成")


@pytest.mark.skip(reason="debug skip")
def test_04(creat_zhiji_random,struct_pho): #04表示第四行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
                                  reqId=get_uuid(),     #必填
                                  gateNo="T1AJ1",      #必填,A B门T1AJ1，复核对应T1AF1
                                  deviceId="T1AJ001",  #必填
                                  cardType="0",         #必填
                                  idCard=zhiji_dic["idNo"],         #必填
                                  nameZh="西瓜",
                                  nameEn="xigua",
                                  age=get_age(zhiji_dic["idNo"]),
                                  sex=1,
                                  birthDate=get_birthday(zhiji_dic["idNo"]),      #必填
                                  address="重庆市",
                                  certificateValidity="20120101-20230202",   #必填
                                  nationality="CHina",
                                  ethnic="汉族",
                                  contactWay="13512134390",
                                  cardPhoto=pho_dic["cardPhoto"],     #必填
                                  fId=get_uuid()       #必填
                                  )
    log(res)


    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
                                     reqId=get_uuid(),  #必填
                                     gateNo="T1AJ1",#必填
                                     deviceId="T1AJ001",#必填
                                     cardType=0,#必填
                                     idCard=zhiji_dic["idNo"],#必填
                                     nameZh="西瓜",
                                     nameEn="xigua",
                                     age=get_age(zhiji_dic["idNo"]),
                                     sex="1",
                                     birthDate=get_birthday(zhiji_dic["idNo"]),#必填
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",#必填
                                     nationality="China",#必填
                                     ethnic="汉族",#必填
                                     contactWay="13512134390",
                                     scenePhoto=pho_dic["scenePhoto"],#必填
                                     sceneFeature=pho_dic["sceneFeature"],#必填
                                     cardPhoto=pho_dic["cardPhoto"],#必填
                                     cardFeature=pho_dic["cardFeature"],#必填
                                     largePhoto=pho_dic["largePhoto"]#必填
                                    )
    log(res)

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=0,  # 类型：0：刷票 1：刷票放行
                                largePhoto="")
    log(res)

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)
    logger.info("test_04测试完成")

@pytest.mark.skip(reason="debug skip")
def test_05(creat_zhiji_random,struct_pho): #05表示第五行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=0,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
                        reqId=get_uuid(),
                        gateNo="T1AF1",
                        deviceId="T1AF002",
                        scenePhoto=pho_dic["scenePhoto"],
                        cardNo=zhiji_dic["idNo"],
                        passengerName="西瓜",
                        passengerEnglishName="xigua",
                        securityStatus=1,#安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
                        securityPassTime=zhiji_dic["lk_chkt"],
                        securityGateNo="",
                        securityDeviceNo="",
                        flightNo=zhiji_dic["lk_flight"],
                        boardingNumber=zhiji_dic["lk_bdno"],
                        sourceType=0,
                        flightDay=zhiji_dic["lk_date"])
    log(res)
    logger.info("test_05测试完成")

@pytest.mark.skip(reason="debug skip")
def test_06(creat_zhiji_random,struct_pho):
    another_pho = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\1.jpg")
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
        reqId=get_uuid(),
        flightNo=zhiji_dic["lk_flight"],
        faceImage=pho_dic["scenePhoto"],
        gateNo="T1AJ1",
        deviceCode="T1AJ002",
        boardingNumber=zhiji_dic["lk_bdno"],
        seatId=zhiji_dic["lk_bdno"],
        startPort="HET",
        flightDay=zhiji_dic["lk_date"][-2:],
        faceFeature=pho_dic["sceneFeature"],
        kindType=0,  # 类型：0：刷票 1：刷票放行
        largePhoto=pho_dic["largePhoto"])

    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
                                  reqId=get_uuid(),     #必填
                                  gateNo="T1AJ1",      #必填,A B门T1AJ1，复核对应T1AF1
                                  deviceId="T1AJ001",  #必填
                                  cardType="0",         #必填
                                  idCard=zhiji_dic["idNo"],         #必填
                                  nameZh="西瓜",
                                  nameEn="xigua",
                                  age=get_age(zhiji_dic["idNo"]),
                                  sex=1,
                                  birthDate=get_birthday(zhiji_dic["idNo"]),      #必填
                                  address="重庆市",
                                  certificateValidity="20120101-20230202",   #必填
                                  nationality="CHina",
                                  ethnic="汉族",
                                  contactWay="13512134390",
                                  cardPhoto=pho_dic["cardPhoto"],     #必填
                                  fId=get_uuid()       #必填
                                  )
    log(res)


    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
                                     reqId=get_uuid(),  #必填
                                     gateNo="T1AJ1",#必填
                                     deviceId="T1AJ001",#必填
                                     cardType=0,#必填
                                     idCard=zhiji_dic["idNo"],#必填
                                     nameZh="西瓜",
                                     nameEn="xigua",
                                     age=get_age(zhiji_dic["idNo"]),
                                     sex="1",
                                     birthDate=get_birthday(zhiji_dic["idNo"]),#必填
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",#必填
                                     nationality="China",#必填
                                     ethnic="汉族",#必填
                                     contactWay="13512134390",
                                     scenePhoto=pho_dic["scenePhoto"],#必填
                                     sceneFeature=pho_dic["sceneFeature"],#必填
                                     cardPhoto=pho_dic["cardPhoto"],#必填
                                     cardFeature=pho_dic["cardFeature"],#必填
                                     largePhoto=another_pho  #必填
                                    )
    log(res)

    """2.3.17安检口人工放行接口（二期）"""

    res = AirportProcess().api_face_security_manual_optcheck(
                                          reqId=get_uuid(),
                                          gateNo="T1AF1",
                                          deviceId="T1AJ001",
                                          cardType=0,
                                          idCard=zhiji_dic["idNo"],
                                          nameZh="西瓜",
                                          nameEn="xigua",
                                          age=get_age(zhiji_dic["idNo"]),
                                          sex="",
                                          birthDate=get_birthday(zhiji_dic["idNo"]),
                                          address="",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=pho_dic["scenePhoto"],
                                          sceneFeature=pho_dic["sceneFeature"],
                                          cardPhoto=pho_dic["cardPhoto"],
                                          cardFeature=pho_dic["cardFeature"],
                                          largePhoto=pho_dic["largePhoto"])

    log(res)

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)
    logger.info("test_06测试完成")

@pytest.mark.skip(reason="debug skip")
def test_07(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)
    logger.debug("test_07测试完成")

@pytest.mark.skip(reason="debug skip")
def test_08(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

    """安检1：1刷证  包括A B 门"""
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填,A B门T1AJ1，复核对应T1AF1
        deviceId="T1AJ001",  # 必填
        cardType="0",  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
        age=get_age(zhiji_dic["idNo"]),
        sex=1,
        birthDate=get_birthday(zhiji_dic["idNo"]),  # 必填
        address="重庆市",
        certificateValidity="20120101-20230202",  # 必填
        nationality="CHina",
        ethnic="汉族",
        contactWay="13512134390",
        cardPhoto=pho_dic["cardPhoto"],  # 必填
        fId=get_uuid()  # 必填
    )
    log(res)

    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填
        deviceId="T1AJ001",  # 必填
        cardType=0,  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
        age=get_age(zhiji_dic["idNo"]),
        sex="1",
        birthDate=get_birthday(zhiji_dic["idNo"]),  # 必填
        address="重庆市",
        certificateValidity="20180101-20260203",  # 必填
        nationality="China",  # 必填
        ethnic="汉族",  # 必填
        contactWay="13512134390",
        scenePhoto=pho_dic["scenePhoto"],  # 必填
        sceneFeature=pho_dic["sceneFeature"],  # 必填
        cardPhoto=pho_dic["cardPhoto"],  # 必填
        cardFeature=pho_dic["cardFeature"],  # 必填
        largePhoto=""  # 必填
    )

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)
    logger.info("test_08测试完成")


@pytest.mark.skip(reason="debug skip")
def test_09(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    another_pho = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\1.jpg")

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=another_pho)
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)
    logger.debug("test_09测试完成")

# @pytest.mark.skip(reason="debug skip")
def test_10(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logger.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
        reqId=get_uuid(),
        flightNo=zhiji_dic["lk_flight"],
        faceImage=pho_dic["scenePhoto"],
        gateNo="T1AJ1",
        deviceCode="T1AJ002",
        boardingNumber=zhiji_dic["lk_bdno"],
        seatId=zhiji_dic["lk_bdno"],
        startPort="HET",
        flightDay=zhiji_dic["lk_date"][-2:],
        faceFeature=pho_dic["sceneFeature"],
        kindType=1,  # 类型：0：刷票 1：刷票放行
        largePhoto=pho_dic["largePhoto"])
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
        reqId=get_uuid(),
        flightNo=zhiji_dic["lk_flight"],
        faceImage=pho_dic["scenePhoto"],
        gateNo="T1AJ1",
        deviceCode="T1AJ002",
        boardingNumber=zhiji_dic["lk_bdno"],
        seatId=zhiji_dic["lk_bdno"],
        startPort="HET",
        flightDay=zhiji_dic["lk_date"][-2:],
        faceFeature=pho_dic["sceneFeature"],
        kindType=1,  # 类型：0：刷票 1：刷票放行
        largePhoto="")
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)

###   核对图片是否存入相应的表里
    connection = connect_db()
    data_list = query_data(connection,"sec_passenger_entity","flight",zhiji_dic["lk_flight"],"bdno",zhiji_dic["lk_bdno"])
    raw_largePhoto_data = ""
    with open(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\0.jpg","rb") as f:
        raw_largePhoto_data = f.read()
    for item in data_list:
        temp_d = query_data(connection,"security_check_info_entity", "ajid", item["ajid"])
        for tmp in temp_d:
            assert tmp["photo"][:100] == raw_largePhoto_data[:100]  #断言 安检信息系统中旅客图片为刷票上传的大图

    connection_t = connect_db(host = "192.168.5.15",db = "htbusyinfo",)
    man_sec_check = query_data(connection_t,"aib_manual_security_check_7_9", "certificate_number", zhiji_dic["idNo"])
    large_photo_path = ""
    for i in man_sec_check:
        if i["large_photo_path"] != "":
            large_photo_path = i["large_photo_path"]
    large_photo_path = "https://192.168.5.15:9090/data-platform-server/api/v1/resource/" + large_photo_path
    res_pho = requests.get(url=large_photo_path, verify=BlackListApi().certificate)
    assert res_pho.content == raw_largePhoto_data  #断言 安检流水表，redis中有上传的大图

    logger.info("%s 测试完成" % sys._getframe().f_code.co_name)



if __name__ == '__main__':
    # pytest.main(["-s", "test_largePhoto_upload.py"])
    pytest.main(["-s","test_largePhoto_upload.py::test_10"])
