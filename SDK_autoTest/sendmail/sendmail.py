#!/usr/bin/python3
# Time : 2019/10/17 16:07 
# Author : zcl
# email.mime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

def sendEmail(content,attachment_list=[]):
    user = "173302591@qq.com"
    pwd = "dbslxetdjojabgge"

    receiver = ["173302591@qq.com","632826078@qq.com"]
    message = MIMEMultipart()
    message['From'] = Header("173302591@qq.com", 'utf-8')
    message['To'] = Header("173302591@qq.com", 'utf-8')
    message['Subject'] = Header("Python 自动化测试报告", 'utf-8')
    message.attach(MIMEText(content, 'html', 'utf-8'))
    os.chdir("../")
    for attachment in attachment_list:
        att = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=%s' % attachment.encode("utf-8")
        message.attach(att)
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login(user, pwd)
        smtpObj.sendmail(user, receiver, message.as_string())
        print("Send Email Successfully...")
    except smtplib.SMTPException as e:
        print("Error: Send Email Failure" + e.strerror)

if __name__ == '__main__':
    # attachs = []
    # conten = open(r"C:\Users\Administrator\IdeaProjects\sendmail\data\result.html","rb").read()
    # # print(conten)
    # sendEmail(conten,attachs)
    # send_normal("HI","<h1>HELLO</h1>")


    # f = open(r"D:\workfile\zhongkeyuan_workspace\SDK_autoTest\analyse_sdk_script\result.html", "rb")
    # c = f.read().decode("utf8","ignore")
    # print(c)







