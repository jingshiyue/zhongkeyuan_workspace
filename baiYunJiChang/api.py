import requests
from BaiTaAirport2_month.common.common_method import *
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from baiYunJiChang.common.method import *

now_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
flightDate = now_date[:10]  # 航班时间，格式为"2019-04-23"
check_in_number = random.randint(1,999)
# captureImg = read_picture(r"D:\pre_data\picture_640_480\0.jpg")
# captureImg_base64 = to_base64(r"D:\pre_data\picture_640_480\7.jpg")
# captureImg_base64 = to_base64(r"C:\Users\admin\Desktop\1.jpg")


class AllApi():
    def __init__(self):
        self.host = "https://175.168.1.199:9191/"
        self.certificate = r"D:\workfile\zhongkeyuan_workspace\baiYunJiChang\common\cacert.crt"      #https证书位置
        self.api_v1_face_security_push_info = self.host + "api/v1/face/security/pushInfo"        #提交旅客验证信息接口url
        self.api_v1_face_review_check = self.host + "api/v1/face/review/check"   #复核口服务器接口url
        # print(self.api_v1_face_security_push_info)
        # print(self.api_v1_face_review_check)

    def  (self,
                                     flightNum="MU5460",                          #必须str    航班号
                                     flightDate=flightDate,                      #必须str    航班日期，格式YYYY-MM-DD
                                     passengerCheckInNumber="1",     #必须str    值机序号
                                     flightBoardingCode="CAN",                   #必须str    始发地（城市名称、3字码）
                                     passengerSeatNumber="1",        #非必须str  座位号
                                     passengerType="02",                         #非必须str  旅客类型  01-婴儿  02-成人
                                     wayCode="F",                                #必须str    通道编号或者闸机编号，参考wayCodeType字段
                                     wayCodeType="way",                          #必须str    说明wayCode的字段类型 way-通道号  gate-闸机编号
                                     passengerIdNum="",                          #非必须str  证件号
                                     passengerIdType="id_card",                  #非必须str  证件类型：id_card–身份证  passport–护照  other–其他
                                     captureImg="",                      #必须byte   全景照  用于提取特征
                                     faceRecognitionImg=b"",                      #非必须byte 人脸识别成功的大头照  不传视为1:1不成功，不保存特征
                                     idImg=b"",                                   #非必须byte 证件头像
                                     name="",                                    #非必须str  旅客姓名
                                     gender="M",                                 #性别str    M-男 F-女
                                     nation="汉族",                              #非必须str  民族
                                     birthday="",                                #非必须str  出生日期, yyyy-mm-dd
                                     validDate="",                               #非必须str  有效日期, yyyy-mm-dd 如无有效期时指定为N/A
                                     address=""              #非必须str  家庭住址
                                     ):
        '''AJ08-提交旅客安检验证信息接口'''
        body = {"flightNum":(None,flightNum),                               #必须str    航班号
                "flightDate":(None,flightDate),                             #必须str    航班日期，格式YYYY-MM-DD
                "passengerCheckInNumber":(None,passengerCheckInNumber),     #必须str    值机序号
                "flightBoardingCode":(None,flightBoardingCode),             #必须str    始发地（城市名称、3字码）
                "passengerSeatNumber":(None,passengerSeatNumber),           #非必须str  座位号
                "passengerType":(None,passengerType),                       #非必须str  旅客类型  01-婴儿  02-成人
                "wayCode":(None,wayCode),                                   #必须str    通道编号或者闸机编号，参考wayCodeType字段
                "wayCodeType":(None,wayCodeType),                           #必须str    说明wayCode的字段类型 way-通道号  gate-闸机编号
                "passengerIdNum":(None,passengerIdNum),                     #非必须str  证件号
                "passengerIdType":(None,passengerIdType),                   #非必须str  证件类型：id_card–身份证  passport–护照  other–其他
                "captureImg":captureImg,                             #必须byte   全景照  用于提取特征
                "faceRecognitionImg":faceRecognitionImg,             #非必须byte 人脸识别成功的大头照  不传视为1:1不成功，不保存特征
                "idImg":idImg,                                       #非必须byte 证件头像
                "name":(None,name),                                         #非必须str  旅客姓名
                "gender":(None,gender),                                     #性别str    M-男 F-女
                "nation":(None,nation),                                     #非必须str  民族
                "birthday":(None,birthday),                                 #非必须str  出生日期, yyyy-mm-dd
                "validDate":(None,validDate),                               #非必须str  有效日期, yyyy-mm-dd 如无有效期时指定为N/A
                "address":(None,address)}                                    #非必须str  家庭住址
        # print(body)
        # headers = {"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryyb1zYhTI38xpQxBK"}      #服务器暂时没做，不验证
        res = requests.post(url=self.api_v1_face_security_push_info,
                            files=body,
                            # headers=headers,
                            verify=self.certificate)
        return res.text

    def api_v1_face_security_pushinfo_must_parameters(self,
                                                     flightNum="MU5460",                          #必须str    航班号
                                                     flightDate=flightDate,                      #必须str    航班日期，格式YYYY-MM-DD
                                                     passengerCheckInNumber="1",     #必须str    值机序号
                                                     flightBoardingCode="CAN",                   #必须str    始发地（城市名称、3字码）
                                                     wayCode="F",                                #必须str    通道编号或者闸机编号，参考wayCodeType字段
                                                     wayCodeType="way",                          #必须str    说明wayCode的字段类型 way-通道号  gate-闸机编号
                                                     captureImg="",                      #必须byte   全景照  用于提取特征
                                                     faceRecognitionImg=b""
                                                    ):
        '''AJ08-提交旅客验证信息接口(只传必须参数)'''
        body = {"flightNum":(None,flightNum),                               #必须str    航班号
                "flightDate":(None,flightDate),                             #必须str    航班日期，格式YYYY-MM-DD
                "passengerCheckInNumber":(None,passengerCheckInNumber),     #必须str    值机序号
                "flightBoardingCode":(None,flightBoardingCode),             #必须str    始发地（城市名称、3字码）
                "wayCode":(None,wayCode),                                   #必须str    通道编号或者闸机编号，参考wayCodeType字段
                "wayCodeType":(None,wayCodeType),                           #必须str    说明wayCode的字段类型 way-通道号  gate-闸机编号
                "captureImg":captureImg,                                     #必须byte   全景照  用于提取特征
                "faceRecognitionImg":faceRecognitionImg
                }

        # headers = {"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryyb1zYhTI38xpQxBK"}      #服务器暂时没做，不验证
        res = requests.post(url=self.api_v1_face_security_push_info,
                            files=body,
                            # headers=headers,
                            verify=self.certificate)
        return res.text

    def api_v1_face_security_pushinfo_new(self,
                                          certificateCode="123456789012345678",   #必须String	    旅客证件号
                                          certificateType="NI",         #非必须String   证件类型：NI –身份证  PP–护照 TP–港澳通行证 TW–台湾通行证 I–外国人永久居民身份证 ID–其他
                                          passengerName="",             #非必须String   旅客姓名
                                          flightNum="MU5460",           #必须String	    航班号
                                          flightDate=flightDate,        #必须String	    航班日期，格式YYYY-MM-DD
                                          passengerCheckInNumber="1",   #必须String     值机序号
                                          passengerSeatNumber="",       #非必须String   座位号
                                          flightBoardingCode="CAN",     #必须String	    始发地（城市名称、3字码）
                                          flightDestCode="WUS",         #必须String	    目的地（城市名称、3字码）
                                          wayCode="123",                #必须String	    通道号（对应凯亚系统的“验证台ID”）
                                          wayName="123",                #必须String     通道名称（对应凯亚系统的“验证台名称”）
                                          checkResult="1",              #必须String	    过检结果：0-不通过 1-通过 2-旅客外出
                                          checkTime=now_date,           #必须String	    过检时间, 格式YYYY-MM-DD HH:mm:ss
                                          boardingTerminal="",          #非必须String   航站楼代号
                                          sealCode="",                  #非必须String   安检电子盖戳
                                          sealType="",                  #非必须String   盖戳类型（验讫类型）
                                          captureImg="",   #必须Base64	    全景照
                                          faceRecognitionImg="",        #非必须Base64	人脸识别成功的大头照
                                          idImg=""                      #非必须Base64	证件头像
                                     ):
        '''2.4.1.	ZK01-旅客过检数据推送接口(新-20190904)'''
        body = {"certificateCode":(None,certificateCode),
                "certificateType":(None,certificateType),
                "passengerName":(None,passengerName),
                "flightNum":(None,flightNum),
                "flightDate":(None,flightDate),
                "passengerCheckInNumber":(None,passengerCheckInNumber),
                "passengerSeatNumber":(None,passengerSeatNumber),
                "flightBoardingCode":(None,flightBoardingCode),
                "flightDestCode":(None,flightDestCode),
                "wayCode":(None,wayCode),
                "wayName":(None,wayName),
                "checkResult":(None,checkResult),
                "checkTime":(None,checkTime),
                "boardingTerminal":(None,boardingTerminal),
                "sealCode":(None,sealCode),
                "sealType":(None,sealType),
                "captureImg":(None,captureImg),
                "faceRecognitionImg":(None,faceRecognitionImg),
                "idImg":(None,idImg)}
        # print(body)
        headers = {"token":"emt5JTNBMTIzNDU2"}
        res = requests.post(url=self.api_v1_face_security_push_info,
                            files=body,
                            headers=headers,
                            verify=self.certificate)
        return res.text

    def api_face_review_check(self,
                              reqId=get_uuid(),
                              gateNo="",
                              deviceId="",
                              scenePhoto="",
                              sceneFeature=""):
        """2.3.6复核口服务器接口（二期优化）"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "scenePhoto": scenePhoto,
                "sceneFeature": sceneFeature}
        # print(self.api_v1_face_review_check)
        res = requests.post(url=self.api_v1_face_review_check,
                            headers=get_headers("/api/v1/face/review/check"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_save(self,
                            reqId=get_uuid(),   #必须
                            ids="",             #流水表记录ID，有就更新，无则增加
                            employeeName="",   #姓名
                            employeeId="",      #员工编号  必须
                            certificateNumber="",       #身份证号码  必须
                            faceImage="",    #人脸图片 base64加密   必须
                            sex=1,           #性别int
                            birthday="",    #出生年月yyyyMMdd
                            position="",    #职务
                            national="",    #民族
                            address="",     #家庭住址
                            contact=""      #联系电话
                            ):
        """白名单增加接口"""
        this_sign = "/api/v1/face/whitelist/save"
        body = {"reqId": reqId,
                "id": ids,  # 32位UUID，流水表记录ID，有就更新，无则增加
                "employeeName": employeeName,
                "employeeId": employeeId,
                "certificateNumber": certificateNumber,
                "faceImage": faceImage,
                "sex":sex,
                "birthday":birthday,
                "position":position,
                "national":national,
                "address":address,
                "contact":contact
                }
        res = requests.post(url=self.host + this_sign,
                            headers=get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_delete(self,
                              this_sign="/api/v1/face/whitelist/delete",
                              reqId=get_uuid(),
                              ids=""):
        """白名单删除接口"""
        body = {"reqId": reqId,
                "ids": ids}
        res = requests.post(url=self.host + this_sign,
                            headers=get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_query(self,
                             reqId=get_uuid(),
                             page=1,       #必须
                             pageSize=1,   #必须
                             employeeName="",
                             employeeId="",        #员工编号
                             certificateNumber="",         #证件号
                             sex=0,         #int 性别
                             isCount=1):   #int 为1的时候查询总记录数
        """白名单查询接口"""
        this_sign = "/api/v1/face/whitelist/query"
        body = {"reqId": reqId,
                "page": page,
                "pageSize": pageSize,
                "employeeName":employeeName,
                "employeeId":employeeId,
                "certificateNumber":certificateNumber,
                "sex":sex,
                "isCount": isCount}
        res = requests.post(url=self.host + this_sign,
                            headers=get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_record_query(self,
                                    reqId=get_uuid(),
                                    channelCode="",    #通道编号
                                    employeeName="",        #姓名
                                    employeeId="",      #员工编号
                                    certificateNumber="",          #证件号
                                    sex=0,           # 性别int
                                    page=1,
                                    pageSize=1,
                                    isCount=1):
        """安检员工记录查询接口"""
        this_sign = "/api/v1/face/whitelist/record/query"
        body = {"reqId": reqId,
                "channelCode": channelCode,
                "employeeName": employeeName,    # 开始时间，格式yyyymmdd。如2018070109
                "employeeId": employeeId,   # 姓名
                "certificateNumber": certificateNumber,
                "sex": sex,
                "page": page,
                "pageSize": pageSize,
                "isCount": isCount}
        res = requests.post(url=self.host + this_sign,
                            headers=get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

if __name__ == '__main__':
    faceImage = to_base64(r'D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\4.jpg')
    # faceImage = to_base64(r'C:\Users\admin\Desktop\2.jpg')
    # faceFeature_2k = read_feature(r'D:\pre_data\picture2k\0.txt')  # 读取一个人脸2k特征值
    # faceFeature_8k = read_feature('D:/pre_data/picture8k/40.txt')  # 读取一个人脸8k特征值
    # res = AllApi().api_v1_face_security_pushinfo_new(certificateCode="123456789012345678",   #必须String	    旅客证件号
    #                                       certificateType="NI",         #非必须String   证件类型：NI –身份证  PP–护照 TP–港澳通行证 TW–台湾通行证 I–外国人永久居民身份证 ID–其他
    #                                       passengerName="",             #非必须String   旅客姓名
    #                                       flightNum="MU5460",           #必须String	    航班号
    #                                       flightDate=flightDate,        #必须String	    航班日期，格式YYYY-MM-DD
    #                                       passengerCheckInNumber="1",   #必须String     值机序号
    #                                       passengerSeatNumber="",       #非必须String   座位号
    #                                       flightBoardingCode="CAN",     #必须String	    始发地（城市名称、3字码）
    #                                       flightDestCode="WUS",         #必须String	    目的地（城市名称、3字码）
    #                                       wayCode="123",                #必须String	    通道号（对应凯亚系统的“验证台ID”）
    #                                       wayName="123",                #必须String     通道名称（对应凯亚系统的“验证台名称”）
    #                                       checkResult="1",              #必须String	    过检结果：0-不通过 1-通过 2-旅客外出
    #                                       checkTime=now_date,           #必须String	    过检时间, 格式YYYY-MM-DD HH:mm:ss
    #                                       boardingTerminal="",          #非必须String   航站楼代号
    #                                       sealCode="",                  #非必须String   安检电子盖戳
    #                                       sealType="",                  #非必须String   盖戳类型（验讫类型）
    #                                       captureImg=faceImage,   #必须Base64	    全景照
    #                                       faceRecognitionImg=faceImage,        #非必须Base64	人脸识别成功的大头照
    #                                       idImg=faceImage                      #非必须Base64	证件头像
    #                                  )
    # print(res)
    res = AllApi().api_white_list_save(ids="",             #流水表记录ID，有就更新，无则增加
                                        employeeName="大西瓜4",   #姓名
                                        employeeId="4",      #员工编号  必须
                                        certificateNumber="500382198808088084",       #身份证号码  必须
                                        faceImage=faceImage,    #人脸图片 base64加密   必须
                                        sex=1,           #性别int
                                        birthday="19880808",    #出生年月yyyyMMdd
                                        position="",    #职务
                                        national="汉",    #民族
                                        address="重庆",     #家庭住址
                                        contact="15555555555"      #联系电话
                                        )
    print(res)
    # print(token_to_base64())

    # print(AllApi().api_v1_face_security_push_info)
    # num = 3
    # captureImg = to_base64(r"D:\pre_data\img(广州)\captureImg%s.jpg"%num)  # 必须Base64	    全景照
    # # faceRecognitionImg = to_base64(r"D:\pre_data\img(广州)\faceRecognitionImg%s.jpg"%num)  # 非必须Base64	人脸识别成功的大头照
    # idImg = to_base64(r"D:\pre_data\img(广州)\idImg%s.jpg"%num)
    # faceRecognitionImg = to_base64(r"D:\pre_data\img(广州)\0.jpg")
    # res = AllApi().api_v1_face_security_pushinfo_new(certificateCode="1234567893",   #必须String	    旅客证件号
    #                                       certificateType="PP",         #非必须String   证件类型：NI –身份证  PP–护照 TP–港澳通行证 TW–台湾通行证 I–外国人永久居民身份证 ID–其他
    #                                       passengerName="",             #非必须String   旅客姓名
    #                                       flightNum="MU5460",           #必须String	    航班号
    #                                       flightDate=flightDate,        #必须String	    航班日期，格式YYYY-MM-DD
    #                                       passengerCheckInNumber="23",   #必须String     值机序号
    #                                       passengerSeatNumber="",       #非必须String   座位号
    #                                       flightBoardingCode="CAN",     #必须String	    始发地（城市名称、3字码）
    #                                       flightDestCode="WUS",         #必须String	    目的地（城市名称、3字码）
    #                                       wayCode="123",                #必须String	    通道号（对应凯亚系统的“验证台ID”）
    #                                       wayName="123",                #必须String     通道名称（对应凯亚系统的“验证台名称”）
    #                                       checkResult="1",              #必须String	    过检结果：0-不通过 1-通过 2-旅客外出
    #                                       checkTime=now_date,           #必须String	    过检时间, 格式YYYY-MM-DD HH:mm:ss
    #                                       boardingTerminal="",          #非必须String   航站楼代号
    #                                       sealCode="",                  #非必须String   安检电子盖戳
    #                                       sealType="",                  #非必须String   盖戳类型（验讫类型）
    #                                       captureImg=captureImg,        #必须Base64	    全景照
    #                                       faceRecognitionImg=faceRecognitionImg,        #非必须Base64	人脸识别成功的大头照
    #                                       idImg=idImg                      #非必须Base64	证件头像
    #                                  )
    #
    # print(res)




