# coding:utf-8
import unittest
from Airport.AllProcesReturnTest.AllProcess import *
import json


class TestAllProcessOne(unittest.TestCase):
    """全流程接口测试用例"""
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ticket_ckeck_1(self):
        """验证能正常验票"""
        body_data1 = {"reqId": get_uuid(),
                      "flightNo": "test1011",
                      "flightDay": produce_flight_date()[6:8],
                      "QTCode": "abcde",
                      "seatId": "3B",
                      "startPort": "1",
                      "boardingNumber": "111"}
        all = AllProcess()
        result = all.api_v1_ticket_check(body_data1)
        dict_data = json.loads(result)
        self.assertEqual(dict_data["result"], 0)

    def test_ticket_ckeck_2(self):
        """验证日期不对时，不能通过验票"""
        body_data1 = {"reqId": get_uuid(),
                      "flightNo": "test1011",
                      "flightDay": "08",
                      "QTCode": "abcde",
                      "seatId": "3B",
                      "startPort": "1",
                      "boardingNumber": "111"}

        all = AllProcess()
        result = all.api_v1_ticket_check(body_data1)
        dict_data = json.loads(result)
        self.assertEqual(dict_data["result"], 0)

    def test_ticket_ckeck_3(self):
        """验证航班号不对时，不能通过验票"""
        body_data1 = {"reqId": get_uuid(),
                      "flightNo": "test1012",
                      "flightDay": produce_flight_date()[6:8],
                      "QTCode": "abcde",
                      "seatId": "3B",
                      "startPort": "1",
                      "boardingNumber": "111"}

        all = AllProcess()
        result = all.api_v1_ticket_check(body_data1)
        dict_data = json.loads(result)
        self.assertEqual(dict_data["result"], 0)

    def test_ticket_ckeck_4(self):
        """验证航班序列号不对时，不能通过验票"""
        body_data1 = {"reqId": get_uuid(),
                      "flightNo": "test1012",
                      "flightDay": produce_flight_date()[6:8],
                      "QTCode": "abcde",
                      "seatId": "3B",
                      "startPort": "1",
                      "boardingNumber": "112"}

        all = AllProcess()
        result = all.api_v1_ticket_check(body_data1)
        dict_data = json.loads(result)
        self.assertEqual(dict_data["result"], 0)


if __name__ == '__main__':
    unittest.main()