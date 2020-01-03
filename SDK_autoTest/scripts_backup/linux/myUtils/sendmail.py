#!/usr/bin/python3
# Time : 2019/10/17 16:07 
# Author : zcl
# email.mime
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

def sendEmail(content,attachment_list=[],env=""):
    user = "173302591@qq.com"
    pwd = "dbslxetdjojabgge"

    receiver = ["173302591@qq.com","728985203@qq.com"]
    message = MIMEMultipart()
    message['From'] = formataddr(["Test", "173302591@qq.com"])  # 发件人邮箱昵称、发件人邮箱账号
    message['To'] = formataddr(["","173302591@qq.com"])
    if "win7_64" in env:
        env = "WIN7 64位"
    if "win7_32" in env:
        env = "WIN7 32位"
    if "linux" in env:
        env = "LINUX"
    message['Subject'] = Header("[EmailTool] SDK自动化测试报告(%s)" %env, 'utf-8')
    message.attach(MIMEText(content, 'html', 'utf-8'))
    for attachment in attachment_list:
        att = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=%s' % attachment.split("/")[-1]
        message.attach(att)
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login(user, pwd)
        smtpObj.sendmail(user, receiver, message.as_string())
        print("Send Email Successfully...")
    except smtplib.SMTPException as e:
        print("Error: Send Email Failure" + e.strerror)

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read(r"./testbed.ini")
    env = config.get("testbed","env")
    html = config.get("testbed","html")
    resultpath = config.get("testbed","resultpath") 
    SdkTestbedF = os.path.join(resultpath,"SdkTestbed.log") 
    monitorF = os.path.join(resultpath,"monitor.png") 
    attachs = [monitorF,SdkTestbedF]
    conten = open(html,"rb").read()
    sendEmail(conten,attachs,env)








