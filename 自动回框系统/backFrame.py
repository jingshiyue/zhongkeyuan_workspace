import requests
import random
# import common
from 自动回框系统.common.common_method import *
from 自动回框系统.common.Idcardnumber import get_random_id_number

class backFrame():
    def __init__(self, host="http://192.168.10.27:10080"):
        self.certificate = None   #用于http
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.host = host
        self._api_airport_face_regist = host + "/api/v1/airport/face/regist"
        self._api_airport_face_recognize = host + "/api/v1/airport/face/recognize"
        self._api_airport_baggage_tracker = host + "/api/v1/airport/baggage/tracker"
        self._api_airport_data_flowback_query = host + "/api/v1/airport/data/flowback-query"
        self._api_airport_baggage_manual_check = host + "/api/v1/airport/baggage/manual-check"
        self._api_airport_regist_records = host + "/api/v1/airport/regist/records"
        self._api_airport_recognize_records = host + "/api/v1/airport/recognize/records"
        self._api_airport_baggage_tracker_detail = host + "/api/v1/airport/baggage/tracker-detail"

 
    def get_headers(self, sign):
        """获取各个接口的请求头"""
        timestamp = get_time_stamp()
        sign = to_md5_str(sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    """1.1 人脸注册接口"""
    def api_airport_face_regist(
            self,
            reqId=get_uuid(),
            cardId=get_random_id_number(),
            cardType=0,
            nameZh="回框测试",
            nameEn="回框测试",
            channelCode='AJ',
            deviceId='T1AJ001',
            flightDate=produce_flight_date(),
            flightNo=produce_flight_number(),
            boardingNo=str(random.randint(1,1000)).zfill(3),
            seatNo=str(random.randint(1,1000)).zfill(3)+'A',
            idImg=to_base64("test_photoes\\picture(现场照片)\\1.jpg"),
            liveImg=to_base64("test_photoes\\picture(现场照片)\\1.jpg"),
            passStatus=1,   #1表示注册成功
            sex=1, #性别0-未知，1-男，2-女

            ):
        body = {
                "reqId":reqId,
                "cardId":cardId,
                "cardType":cardType,
                "channelCode":channelCode,
                "deviceId":deviceId,
                "flightDate":flightDate,
                "flightNo":flightNo,
                "boardingNo":boardingNo,
                "seatNo":seatNo,
                "idImg":idImg,
                "liveImg":liveImg,
                "nameZh":nameZh,
                "nameEn":nameEn,
                "passStatus":passStatus,
                "sex":sex,
                }

        res = requests.post(url=self._api_airport_face_regist,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/face/regist"),
                            verify=self.certificate)
        res.close()
        return res

    """1.2 人脸识别行李绑定接口"""
    def api_airport_face_recognize(
            self,
            reqId=get_uuid(),
            rfid='1001',
            deviceId='T1AJ001',
            channelCode='AJ',
            scenePhoto=to_base64("test_photoes\\picture(现场照片)\\1.jpg"),
            sceneFeature="",
            # position=[{"top":1,"left":1,"right":1,"bottom":1}],
            ):
        body = {
                "reqId":reqId,
                "rfid":rfid,
                "deviceId":deviceId,
                "channelCode":channelCode,
                "scenePhoto":scenePhoto,
                "sceneFeature":sceneFeature,
                }
        # print(body)
        # print(self.get_headers("/api/v1/face/security/ticket-check"))
        print("url:"+self._api_airport_face_recognize)
        print(self.get_headers("/api/v1/airport/face/recognize"))
        res = requests.post(url=self._api_airport_face_recognize,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/face/recognize"),
                            verify=self.certificate)
        res.close()
        return res


    """1.3 行李轨迹绑定接口"""
    def api_airport_baggage_tracker(
            self,
            reqId=get_uuid(),
            baseDeviceId='',
            channelCode='AJ',
            rfid='1001',
            processNode='',
            extraInfo={},
            imgs='',
            ):
        body = {
                "reqId":reqId,
                "baseDeviceId":baseDeviceId,
                "channelCode":channelCode,
                "rfid":rfid,
                "processNode":processNode,
                "extraInfo":extraInfo,
                "imgs":imgs
                }

        res = requests.post(url=self._api_airport_baggage_tracker,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/baggage/tracker"),
                            verify=self.certificate)
        res.close()
        return res

    """1.4 人员回查接口"""
    def api_airport_data_flowback_query(
            self,
            reqId=get_uuid(),
            cardId='',
            flightNo='',
            flightDay='',
            boardingNumber='',
            isFuzzyQuery='',
            seatId='',
            ):
        body = {
                "reqId":reqId,
                "cardId":cardId,
                "flightNo":flightNo,
                "flightDay":flightDay,   #航班dd
                "boardingNumber":boardingNumber,
                "isFuzzyQuery":isFuzzyQuery,
                "seatId":seatId
                }

        res = requests.post(url=self._api_airport_data_flowback_query,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/data/flowback-query"),
                            verify=self.certificate)
        res.close()
        return res

    """1.5 人工放行行李绑定接口"""
    def api_airport_baggage_manual_check(
            self,
            reqId=get_uuid(),
            rfid='',
            baseDeviceId='',
            channelCode='',
            largeImg='',
            flightNumber='',
            flightDay='',
            boardingNumber='',
            kindType='', #类型：0-放行，1-报警
            certificateType='',
            certificateNumber='',
            passengerName='',
            passengerSex='',
            ):
        body = {
                "reqId":reqId,
                "rfid":rfid,
                "baseDeviceId":baseDeviceId,
                "channelCode":channelCode,
                "largeImg":largeImg,
                "flightNumber":flightNumber,
                "flightDay":flightDay,
                "boardingNumber":boardingNumber,
                "kindType":kindType,
                "certificateType":certificateType,
                "certificateNumber":certificateNumber,
                "passengerName":passengerName,
                "passengerSex":passengerSex,
                }

        res = requests.post(url=self._api_airport_baggage_manual_check,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/baggage/manual-check"),
                            verify=self.certificate)
        res.close()
        return res


    """2.1 人脸注册记录查询"""
    def api_airport_regist_records(
            self,
            reqId=get_uuid(),
            pageNum='',
            pageSize='',
            isCount='',

            certificateNumber='',
            passengerName='',
            passengerEnglishName='',
            channelCode='',
            startTime='',
            endTime='',
            passStatus='',
            ):
        body = {
                "reqId":reqId,
                "pageNum":pageNum,
                "pageSize":pageSize,
                "isCount":isCount,
                "certificateNumber":certificateNumber,
                "passengerName":passengerName,
                "passengerEnglishName":passengerEnglishName,
                "channelCode":channelCode,
                "startTime":startTime,
                "endTime":endTime,
                "passStatus":passStatus,
                }

        res = requests.post(url=self._api_airport_regist_records,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/regist/records"),
                            verify=self.certificate)
        res.close()
        return res


    """2.2 旅客识别记录查询"""
    def api_airport_recognize_records(
            self,
            reqId=get_uuid(),
            pageNum='',
            pageSize='',
            isCount='',
            certificateNumber='',
            ):
        body = {
                "reqId":reqId,
                "pageNum":pageNum,
                "pageSize":pageSize,
                "isCount":isCount,
                "certificateNumber":certificateNumber,
                }

        res = requests.post(url=self._api_airport_recognize_records,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/recognize/records"),
                            verify=self.certificate)
        res.close()
        return res


    """2.3 托盘轨迹查询"""
    def api_airport_baggage_tracker_detail(
            self,
            reqId=get_uuid(),
            locusId=""
            ):
        body = {
                "reqId":reqId,
                "locusId":locusId,
                }

        res = requests.post(url=self._api_airport_baggage_tracker_detail,
                            json=body,
                            headers=self.get_headers("/api/v1/airport/baggage/tracker-detail"),
                            verify=self.certificate)
        res.close()
        return res



if __name__ == '__main__':
    num = str(random.randint(1,1000)).zfill(3)
    res = backFrame().api_airport_face_regist(
                                                boardingNo=num,seatNo=num+'A',
                                                cardId='500382199909091001',
                                                idImg=to_base64(r"D:\workfile\zhongkeyuan_workspace\pic\1.jpg"),
                                                liveImg=to_base64(r"D:\workfile\zhongkeyuan_workspace\pic\1.jpg"),
                                                )

    
    print(res.text)