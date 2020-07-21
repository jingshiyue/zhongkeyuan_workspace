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

    cardId = "500382199909090114"
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

    time.sleep(3)

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
    # test_process_01()
    # test_process_02()
    # time.sleep(10)
    # test_process_03()
    # test_07()
    test_04()

