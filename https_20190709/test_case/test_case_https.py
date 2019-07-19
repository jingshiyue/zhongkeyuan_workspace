import unittest,json
from https_20190709.common.common_method import *
from https_20190709.API_https.AirportProcess import AirportProcess
from https_20190709.API_https.BlackList import BlackListApi

class TestCaseHTTPS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.airport_process = AirportProcess()
        cls.black_list = BlackListApi()

    def test_01(self):
        """验证传入未值机旅客信息，服务器能正常响应"""
        idCard = "123456789012345678"
        cardPhoto = to_base64("D:/pre_data/picture(现场照片)/1.jpg")
        res = self.airport_process.api_security_ticket_check(gateNo="T1AJ1",
                                                              deviceId="T1AJ001",
                                                              cardType="0",
                                                              idCard=idCard,
                                                              nameZh="nameZh",
                                                              nameEn="nameEn",
                                                              age=None,
                                                              sex=None,
                                                              birthDate=get_birthday(idCard),
                                                              address="重庆市",
                                                              certificateValidity="20120101-20230202",
                                                              nationality="CHina",
                                                              ethnic="汉族",
                                                              contactWay="0123456789",
                                                              cardPhoto=cardPhoto,
                                                              )
        print(res.text)
        result = json.loads(res.text)
        self.assertEqual(result["status"],0)
        self.assertEqual(result["msg"],"Success")
        self.assertEqual(result["result"],1)

    def test_02(self):
        '''验证传入已值机旅客信息，服务器能正常响应'''
        idCard = "123456789012345678"
        cardPhoto = to_base64("D:/pre_data/picture(现场照片)/1.jpg")
        res = self.airport_process.api_security_ticket_check(gateNo="T1AJ1",
                                                             deviceId="T1AJ001",
                                                             cardType="0",
                                                             idCard=idCard,
                                                             nameZh="nameZh",
                                                             nameEn="nameEn",
                                                             age=None,
                                                             sex=None,
                                                             birthDate=get_birthday(idCard),
                                                             address="重庆市",
                                                             certificateValidity="20120101-20230202",
                                                             nationality="CHina",
                                                             ethnic="汉族",
                                                             contactWay="0123456789",
                                                             cardPhoto=cardPhoto,
                                                             )
        result = json.loads(res.text)
        self.assertEqual(result["status"], 0)
        self.assertEqual(result["msg"], "Success")
        self.assertEqual(result["result"], 1)

if __name__ == '__main__':
    pass

