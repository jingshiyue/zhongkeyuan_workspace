import pytest
from 自动回框系统.backFrame import *
import time


bf = backFrame()

def test_01():
    """1.1 人脸注册接口"""
    res = bf.api_airport_face_regist(
            reqId=get_uuid(),
            cardId='500382199909090013',
            cardType=0,
            nameZh="回框测试13",
            nameEn="回框测试13",
            channelCode='AJ',
            deviceId='T1AJ001',
            flightDate="20200716",
            flightNo="G52873",
            boardingNo=str(random.randint(1,1000)).zfill(3),
            seatNo=str(random.randint(1,1000)).zfill(3)+'A',
            idImg=to_base64("test_photoes\\picture(现场照片)\\13.jpg"),
            liveImg=to_base64("test_photoes\\picture(现场照片)\\13.jpg"),
            passStatus=1,
    )
    print(res.text)


def test_02():
    """1.2 人脸识别行李绑定接口   自动绑定"""
    import base64
    from 自动回框系统.common.sqlTool import DataBase
    shujuku = DataBase("192.168.10.27", 3306, "root", "123456", "back_frame")
    shujuku.open_data_base()
    sql = "select CertificateNumber,FeartureInfo FROM face_review_feature where CertificateNumber='500382199909090012';"
    data = shujuku.find_all(sql)
    temp = data[0][1]
    feature = base64.b64encode(temp)
    feature = (str(feature)[2:-1])
    
    res = bf.api_airport_face_recognize(
            reqId=get_uuid(),
            rfid='2222',
            scenePhoto=to_base64("test_photoes\\picture(现场照片)\\4.jpg"), #旅客的现场图片
            sceneFeature=feature,  #旅客的现场图片特征
    )
    print(res.text)

def test_03_01():
    """x 光机前"""
    res = bf.api_airport_baggage_tracker(
        reqId=get_uuid(),
        baseDeviceId='T1AJ001',
        channelCode='AJ',
        rfid='2222',
        processNode=1,
        extraInfo={},
        imgs=[{"photoName":"x 光机前","imgData":to_base64("test_photoes\\picture(现场照片)\\4.jpg")}],
    )
    print(res.text)

def test_03_02(isRecheck):
    """x 光机后  带复查框指定结果+图片"""
    res = bf.api_airport_baggage_tracker(
        reqId=get_uuid(),
        baseDeviceId='T1AJ001',
        channelCode='AJ',
        rfid='2222',
        processNode=2,
        extraInfo={"isRecheck":isRecheck},  #节点=2，出x光机后填写。是否拆包复检 1: 是 0：否
        imgs=[{"photoName":"x 光机后","imgData":to_base64("test_photoes\\picture(现场照片)\\4.jpg")}],
    )
    print(res.text)

def test_03_03(result):
    """3-空框注册与判别中最后一格（带判别结果+图片）"""
    res = bf.api_airport_baggage_tracker(
        reqId=get_uuid(),
        baseDeviceId='T1AJ001',
        channelCode='AJ',
        rfid='2222',
        processNode=3,
        extraInfo={"checkResult":result},  #节点3和4空框检查填写。空框结果0-无物品 1-有物品 
        imgs=[{"photoName":"3-空框注册与判别中最后一格","imgData":to_base64("test_photoes\\picture(现场照片)\\4.jpg")}],
    )
    print(res.text)


def test_03_04(result):
    """4-空框注册与判别中倒框位置（带判别结果+图片）"""
    res = bf.api_airport_baggage_tracker(
        reqId=get_uuid(),
        baseDeviceId='T1AJ001',
        channelCode='AJ',
        rfid='2222',
        processNode=4,
        extraInfo={"checkResult":0},  #节点3和4空框检查填写。空框结果0-无物品 1-有物品 
        imgs=[{"photoName":"4-空框注册与判别中倒框位置","imgData":to_base64("test_photoes\\picture(现场照片)\\4.jpg")}],
    )
    print(res.text)

def test_03_05():
    """5-回框准备中复查框位   要加图片"""
    res = bf.api_airport_baggage_tracker(
        reqId=get_uuid(),
        baseDeviceId='T1AJ001',
        channelCode='AJ',
        rfid='2222',
        processNode=5,
        extraInfo={"rfId":"2223"},  #节点5填写。填写主的rfid
        imgs=[{"photoName":"5-回框准备中复查框位","imgData":to_base64("test_photoes\\picture(现场照片)\\4.jpg")}],
    )
    print(res.text)

def test_03_06():
    """6-回框准备中空框回流位  要加图片"""
    res = bf.api_airport_baggage_tracker(
        reqId=get_uuid(),
        baseDeviceId='T1AJ001',
        channelCode='AJ',
        rfid='2222',
        processNode=6,
        imgs=[{"photoName":"6-回框准备中空框回流位","imgData":to_base64("test_photoes\\picture(现场照片)\\4.jpg")}],
    )
    print(res.text)

def test_03_07():
    """7-回框准备中空框开包位"""
    res = bf.api_airport_baggage_tracker(
        reqId=get_uuid(),
        baseDeviceId='T1AJ001',
        channelCode='AJ',
        rfid='2222',
        processNode=7,
        imgs=[{"photoName":"7-回框准备中空框开包位","imgData":to_base64("test_photoes\\picture(现场照片)\\4.jpg")}],
    )
    print(res.text)

def test_04():
    """1.4 人员回查接口"""
    res = bf.api_airport_data_flowback_query(
            reqId=get_uuid(),
            cardId='500103199410141531',
            # flightNo='G52873',
            # flightDay='20',  #	航班dd
            # boardingNumber='864',
            # isFuzzyQuery=0,
            # seatId='864A',
    )
    print(res.text)

def test_05():
    """1.5 人工放行行李绑定接口"""
    res = bf.api_airport_baggage_manual_check(
            reqId=get_uuid(),
            rfid='2222',
            baseDeviceId='T1AJ001',
            channelCode='AJ',
            largeImg=to_base64("test_photoes\\picture(现场照片)\\13.jpg"),
            flightNumber='G52873',
            flightDay='20200716',
            boardingNumber='235',
            kindType=0,#类型：0-放行，1-报警
    )
    print(res.text)

def test_06():
    """2.1 人脸注册记录查询"""
    res = bf.api_airport_regist_records(
            reqId=get_uuid(),
            pageNum=1,
            pageSize=100,
            isCount=1,
                        
            certificateNumber='',
            passengerName='回框测试01',
            passengerEnglishName='',
            channelCode='',
            startTime='',
            endTime='',
            passStatus='',
    )
    print(res.text)

def test_07():
    """2.2 旅客识别记录查询"""
    res = bf.api_airport_recognize_records(
            reqId=get_uuid(),
            pageNum=1,
            pageSize=100,
            isCount=1,
            certificateNumber='500382199909090104'
            
    )
    print(res.text)

def test_08():
    """2.3 托盘轨迹查询"""
    res = bf.api_airport_baggage_tracker_detail(
            reqId=get_uuid(),
            locusId='4d86be0dbdb1472eaa1a9433a0d5a278',
    )
    print(res.text)

def test_process_01():
    """注册+系统绑定"""

    cardId = "500382199909090116"
    nameZh="回框测试" + cardId[-3:]
    nameEn="回框测试" + cardId[-3:]
    flightNo="G52873"
    flightDate=produce_flight_date()
    boardingNo=str(random.randint(1,1000)).zfill(3)
    seatNo=boardingNo+'A'
    idImg=to_base64("test_photoes\\picture(现场照片)\\%s.jpg" %cardId[-3:])
    liveImg=to_base64("test_photoes\\picture(现场照片)\\%s.jpg" %cardId[-3:])

    """注册"""
    res = bf.api_airport_face_regist(
            reqId=get_uuid(),
            cardId=cardId,
            cardType=0,
            nameZh=nameZh,
            nameEn=nameEn,
            channelCode='AJ',
            deviceId='T1AJ001',
            flightDate=flightDate,
            flightNo=flightNo,
            boardingNo=boardingNo,
            seatNo=seatNo,
            idImg=idImg,
            liveImg=liveImg,
            passStatus=1,
    )
    print("注册: " + res.text)

    time.sleep(10)

    """系统绑定"""
    # import base64
    # from 自动回框系统.common.sqlTool import DataBase
    # shujuku = DataBase("192.168.10.27", 3306, "root", "123456", "back_frame")
    # shujuku.open_data_base()
    # sql = "select CertificateNumber,FeartureInfo FROM face_review_feature where CertificateNumber='%s';" %cardId
    # data = shujuku.find_all(sql)
    # temp = data[0][1]
    # feature = base64.b64encode(temp)
    # feature = (str(feature)[2:-1])
    
    # res = bf.api_airport_face_recognize(
    #         reqId=get_uuid(),
    #         rfid='2222',
    #         scenePhoto=to_base64("test_photoes\\picture(现场照片)\\4.jpg"),  #旅客的安检现场图片
    #         sceneFeature=feature,  #旅客的现场图片特征
    # )
    # print("系统绑定: " + res.text)

    res = bf.api_airport_face_recognize(
            reqId=get_uuid(),
            rfid='2222',
            scenePhoto=to_base64("test_photoes\\picture(现场照片)\\4.jpg"),  #旅客的安检现场图片
            sceneFeature='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')
    print("系统绑定: " + res.text)

def test_process_02():
    """注册+回查+人工绑定"""

    cardId = "500382199909090106"
    nameZh="回框测试" + cardId[-3:]
    nameEn="回框测试" + cardId[-3:]
    flightNo="G52873"
    flightDate=produce_flight_date()
    boardingNo=str(random.randint(1,1000)).zfill(3)
    seatNo=boardingNo+'A'
    idImg=to_base64("test_photoes\\picture(现场照片)\\%s.jpg" %cardId[-3:])
    liveImg=to_base64("test_photoes\\picture(现场照片)\\%s.jpg" %cardId[-3:])
    largeImg = to_base64("test_photoes\\picture(现场照片)\\%s.jpg" %cardId[-3:])
    """注册"""
    res = bf.api_airport_face_regist(
            reqId=get_uuid(),
            cardId=cardId,
            cardType=0,
            nameZh=nameZh,
            nameEn=nameEn,
            channelCode='AJ',
            deviceId='T1AJ001',
            flightDate=flightDate,
            flightNo=flightNo,
            boardingNo=boardingNo,
            seatNo=seatNo,
            idImg=idImg,
            liveImg=liveImg,
            passStatus=1,
    )
    print("注册: " + res.text)
    time.sleep(30)

    """系统绑定"""
    import base64
    from 自动回框系统.common.sqlTool import DataBase
    shujuku = DataBase("192.168.10.27", 3306, "root", "123456", "back_frame")
    shujuku.open_data_base()
    sql = "select CertificateNumber,FeartureInfo FROM face_review_feature where CertificateNumber='%s';" %cardId
    data = shujuku.find_all(sql)
    temp = data[0][1]
    feature = base64.b64encode(temp)
    feature = (str(feature)[2:-1])[:-3] + "sb"
    
    res = bf.api_airport_face_recognize(
            reqId=get_uuid(),
            rfid='2222',
            scenePhoto=to_base64("test_photoes\\picture(现场照片)\\4.jpg"),  #旅客的安检现场图片
            sceneFeature=feature,  #旅客的现场图片特征
    )
    print("系统绑定: " + res.text)
    time.sleep(5)
    print(flightDate)
    """1.4 人员回查接口"""
    res = bf.api_airport_data_flowback_query(
            reqId=get_uuid(),
            # cardId='500382199909090011',
            flightNo=flightNo,
            flightDay=flightDate[-2:],  #	航班dd
            boardingNumber=boardingNo,
            isFuzzyQuery=0,
            # seatId='874A',
    )
    print("回查: " + res.text)
    time.sleep(1)
    """1.5 人工放行行李绑定接口"""
    res = bf.api_airport_baggage_manual_check(
            reqId=get_uuid(),
            rfid='2222',
            baseDeviceId='T1AJ001',
            channelCode='AJ',
            largeImg=largeImg,
            flightNumber=flightNo,
            flightDay=flightDate,
            boardingNumber=boardingNo,
            kindType=1,#类型：0-放行，1-报警
            certificateType=0,
            certificateNumber=cardId,
            passengerName=nameZh,
            passengerSex=2,
    )
    print("人工放行: " + res.text)
    
    time.sleep(30)
    """1.4 人员回查接口"""
    res = bf.api_airport_data_flowback_query(
            reqId=get_uuid(),
            # cardId='500382199909090011',
            flightNo=flightNo,
            flightDay=flightDate[-2:],  #	航班dd
            boardingNumber=boardingNo,
            isFuzzyQuery=0,
            # seatId='594A',
    )
    print("回查: " + res.text)


def test_process_03():
    """一次性通过"""
    test_03_01()   #x 前
    print("*"*66)
    test_03_02(0)  #x 后
    print("*"*66)
    test_03_03(0)  #3-空框注册与判别中最后一格（带判别结果+图片），
    print("*"*66)
    test_03_04(0) #4-空框注册与判别中倒框位置（带判别结果+图片）
    print("*"*66)
    test_03_06()
    print("*"*66)

def test_process_04():
    """做2次复查通过"""
    test_03_01()   #x 前
    print("*"*66)
    test_03_02(1)  #x 后  是否拆包复检 1: 是 0：否
    print("*"*66)
    test_03_05()  #复检
    print("*"*66)

    test_03_01()   #x 前
    print("*"*66)
    test_03_02(1)  #x 后  是否拆包复检 1: 是 0：否
    print("*"*66)
    test_03_05()
    print("*"*66)
    test_03_01()   #x 前
    print("*"*66)
    test_03_02(0)  #x 后  是否拆包复检 1: 是 0：否
    print("*"*66)
    test_03_03(0)  #3-空框注册与判别中最后一格（带判别结果+图片），
    print("*"*66)
    test_03_04(0) #4-空框注册与判别中倒框位置（带判别结果+图片）
    print("*"*66)
    test_03_06()
    print("*"*66)

    # test_03_03(0)  #3-空框注册与判别中最后一格（带判别结果+图片），
    # print("*"*66)
    # test_03_04(0) #4-空框注册与判别中倒框位置（带判别结果+图片）
    # print("*"*66)
    # test_03_06()
    # print("*"*66)

if __name__ == "__main__":
    test_process_01()
    # test_process_02()
    # time.sleep(10)
    # test_process_03()
    # test_07()
    # test_04()

