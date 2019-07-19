# coding:utf-8
import requests
from Airport.new_method import *
from Airport.msgQueue.Autosendlk import send_lkxx,send_ajxx
from Airport.id.Idcardnumber import *
from Airport.id.new_xingm import get_name
from xpinyin import Pinyin


class AllProcess(object):
    """全流程接口调用方法"""

    def __init__(self):
        self.url_pre_check_ticket = "http://192.168.0.234:9090/presecurity-server/api/v1/ticket/check"
        self.url_pre_sec = "http://192.168.0.234:9090/presecurity-server/api/v1/face/pre-security/check"
        self.url_sec = "http://192.168.0.234:9090/security-server/api/v1/face/security/check"
        self.url_review = "http://192.168.0.234:9090/review-server/api/v1/face/review/check"
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    @staticmethod
    def get_dir_text(dir):
        """获取目录下的txt文件的内容"""
        with open(dir, "r") as fp:
            data = str(fp.read()).rstrip()
        return data

    def get_header(self, new_add_sign):
        """获取各个接口的header"""
        timestamp = get_time_stamp()
        sign = to_md5_str(new_add_sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp":timestamp}
        return header

    def api_v1_ticket_check(self, body, sign_only="/api/v1/ticket/check"):
        """验票接口"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.url_pre_check_ticket,
                            headers=header,
                            json=body,
                            verify=False)
        print(res.text)
        return res.text

    def api_v1_face_pre_security_check(self, body,sign_only="/api/v1/face/pre-security/check"):
        """预安检人脸验证接口"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.url_pre_sec,
                            headers=header,
                            json=body,
                            verify=False)
        print(res.text)
        return res.text

    def api_v1_face_security_check(self,body,sign_only="/api/v1/face/security/check"):
        """安检口人脸验证"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.url_sec,
                            headers=header,
                            json=body,
                            verify=False)
        print(res.text)
        return res.text

    def api_v1_face_review_check(self, body,sign_only="/api/v1/face/review/check"):
        """复核口验证"""
        header = self.get_header(sign_only)
        res = requests.post(url=self.url_review,
                            headers=header,
                            json=body,
                            verify=False)
        print(res.text)
        return res.text

    def get_id_features(self, a):
        base_dir = "E:\\test1000标准\\id1000features\\"
        data = self.get_dir_text(base_dir+"%d" % a + ".jpg" + "\\0.txt")
        return data

    def get_live_features(self, a):
        base_dir = "E:\\test1000标准\\live1000features\\"
        data = self.get_dir_text(base_dir + "%d" % a + ".jpg" + "\\0.txt")
        return data

    @staticmethod
    def get_id_base64(a):
        base_dir = "E:\\test1000标准\\idphoto\\"
        data = to_base64(base_dir+"%d" % a + ".jpg")
        return data

    @staticmethod
    def get_live_base64(a):
        base_dir = "E:\\test1000标准\\livephoto\\"
        data = to_base64(base_dir + "%d" % a + ".jpg")
        return data

    def get_n_features(self, a):
        base_dir = "E:\\test1000标准\\识别features\\"
        data = self.get_dir_text(base_dir+"%d" % a+".jpg"+"\\0.txt")
        return data

    @staticmethod
    def send_allprocess(idcard, flight, lk_name, lk_bdno,m):
        process = AllProcess()
        send_lkxx(lk_cardid=idcard, lk_chkt=get_zhiji(h=2), lk_cname=lk_name,
                  lk_date=produce_flight_date(),
                  lk_flight=flight,
                  lk_id=get_uuid(),
                  lk_bdno=lk_bdno,
                  lk_insur="1"
                  )
        time.sleep(1)
        body1 = {"reqId": get_uuid(),
                 "flightNo": flight,
                 "flightDay": produce_flight_date()[6:8],
                 "QTCode": "abcde",
                 "seatId": "3B",
                 "startPort": "1",
                 "boardingNumber": lk_bdno}

        body2 = {"reqId": get_uuid(),
                 "gateNo": "T1YA1",
                 "deviceId": "T1YA001",
                 "cardType": 0,  # 证件类型 int
                 "idCard": idcard,
                 "nameZh": lk_name,
                 "nameEn": "CHENKEYUN",
                 "age": 25,  # int
                 "sex": 1,  # int
                 "birthDate": get_birthday(idcard),
                 "address": "重庆市大竹林街道",
                 "certificateValidity": "20081010-20191206",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": "中国",
                 "ethnic": "汉族",
                 "contactWay": "18680946659",
                 "scenePhoto": process.get_live_base64(m),
                 "sceneFeature": process.get_live_features(m),
                 "cardPhoto": process.get_id_base64(m),
                 "cardFeature": process.get_id_features(m),
                 "flightNo": flight,
                 "flightDay": produce_flight_date()[6:8],
                 "QTCode": "abcde",
                 "seatId": "3B",
                 "startPort": "1",
                 "boardingNumber": lk_bdno,
                 "fId": get_uuid()}
        body3 = {"reqId": get_uuid(),
                 "gateNo": "T1AJ1",
                 "deviceId": "T1AJ001",
                 "cardType": 0,  # 证件类型 int
                 "idCard": idcard,
                 "nameZh": lk_name,
                 "nameEn": "CHENKEYUN",
                 "age": 25,  # int
                 "sex": 1,  # int
                 "birthDate": get_birthday(idcard),
                 "address": "重庆市大竹林街道",
                 "certificateValidity": "20081010-20191206",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": "中国",
                 "ethnic": "汉族",
                 "contactWay": "18680946659",
                 "scenePhoto": process.get_live_base64(m),
                 "sceneFeature": process.get_live_features(m),
                 "cardPhoto": process.get_id_base64(m),
                 "cardFeature": process.get_id_features(m)}
        body4 = {"reqId": get_uuid(),
                 "gateNo": "T1AF1",
                 "deviceId": "T1AF001",
                 "scenePhoto": process.get_live_base64(m),
                 "sceneFeature": process.get_n_features(m)
                 }
        # 全流程
        process.api_v1_ticket_check(body1)
        process.api_v1_face_pre_security_check(body2)
        time.sleep(1.5)
        process.api_v1_face_security_check(body3)
        time.sleep(1.5)
        process.api_v1_face_review_check(body4)


if __name__ == '__main__':
    process = AllProcess()
    id_features = process.get_dir_text(r"E:\test1000标准\id1000features\1.jpg\0.txt")
    live_features = process.get_dir_text(r"E:\test1000标准\live1000features\1.jpg\0.txt")
    id_base64 = to_base64(r"E:\test1000标准\idphoto\1.jpg")
    live_base64 = to_base64(r"E:\test1000标准\livephoto\1.jpg")
    N_features = process.get_dir_text(r"E:\test1000标准\识别features\1.jpg\0.txt")
    # 半流程  直接通过安检然后再复核
    body5 = {"reqId": get_uuid(),
             "gateNo": "T1AJ2",
             "deviceId": "T1AJ002",
             "cardType": 0,  # 证件类型 int
             "idCard": "500238199312134391",
             "nameZh": "chenkeyun",
             "nameEn": "CHENKEYUN",
             "age": 25,  # int
             "sex": 1,  # int
             "birthDate": "19931213",
             "address": "重庆市渝北区光电园",
             "certificateValidity": "20181109-长期",  # 时间yyyymmdd或者长期(起-止)
             "nationality": "中国",
             "ethnic": "汉族",
             "contactWay": "13888888888",
             "scenePhoto": process.get_live_base64(4),
             "sceneFeature": process.get_live_features(4),
             "cardPhoto": process.get_id_base64(4),
             "cardFeature": process.get_id_features(4)}

    body6 = {"reqId": get_uuid(),
             "gateNo": "T1AF2",
             "deviceId": "T1AF002",
             "scenePhoto": process.get_live_base64(4),
             "sceneFeature": process.get_n_features(4)
             }
    # process.api_v1_face_security_check(body5)
    # time.sleep(1)
    # process.api_v1_face_review_check(body6)
    AllProcess.send_allprocess(idcard=get_random_id_number(), flight="MU00" + str(165),
                               lk_name=get_name(), lk_bdno="165", m=165)
    # a = 160
    # while a < 170:
    #     AllProcess.send_allprocess(idcard=get_random_id_number(),flight="MU00"+str(a),
    #                                lk_name=get_name(), lk_bdno=str(random.randint(100,999)), m=a)
    #     a += 1
    #     time.sleep(1)

    # A = Pinyin()
    # m = A.convert_pinyin(word="nh",convert='upper')
    # k = A.get_pinyin(chars="你好",splitter="",convert="upper")
    # print(k)
    # print(m)
    # print(ord("哈"))











