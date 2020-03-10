#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version: v1.0
@author:Colin
@file: email_sender.py
@time: 3/9/2020/4:49 PM
"""

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
import config


sender = config.Email
receiver = config.Receiver
currency = config.Currency

def login_mail_stmp():
    try:
        smtp = SMTP_SSL(config.Host_server)
        #参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(config.Host_server)
        smtp.login(config.Email, config.Email_passwod)
        print("邮箱登录成功")
        return smtp
    except Exception as e:
        print("登录失败","请检查你的发件邮箱配置",e)
        exit()

def send_request_mail(crude_price, updata_time, remarks = ""):
    print("开始连接smtp服务并进行登录")
    smtp = login_mail_stmp()
    mail_content = "当前原油价格为{0},更新时间{1},".format(crude_price,updata_time) + '符合你的期望价格<a href = "http://gu.sina.cn/ft/hq/hf.php?symbol=CL&autocallup=no">点击查看详情</a>'
    msg = MIMEMultipart()
    print("当前原油价格为{0}{1}{2}".format(crude_price,currency,updata_time) + remarks)
    mail_title = "当前原油价格为{0}{1},".format(crude_price,currency) + remarks

    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = formataddr(["纽约原油价格监控助手", sender])
    msg["To"] = Header(receiver[0])
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    try:
        smtp.sendmail(sender, receiver, msg.as_string())
        print("发送成功，接收人：",receiver)
        print("=" * 100)
    except Exception as e:
        print("发送失败","请检查你的收件邮箱",e)
        exit()

