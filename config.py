#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version: v1.0
@author:Colin
@file: config.py
@time: 3/9/2020/4:19 PM
"""
# 原油价格的低价购入提醒，如不修改汇率需设置为美元，可设置多个，设置一个举例：Minimum_reminder = [27]
#设置多个举例： Minimum_reminder = [27, 28.5, 29]
Minimum_reminder = [28, 27]
#原油价格高价卖出提醒
Highest_reminder = [40]
#设置监控类型，0代表监控低价，1代表监控高价
Reminder_type = 0


#设置发送邮件的邮箱
Host_server = 'smtp.qq.com'
Email = 'icktime@qq.com'
Email_passwod = 'czizkaacaupwbbdf'

#设置接受邮箱,添加多个用逗号隔开
Receiver = ['icktime@163.com']

#原油价格刷新频率，以秒为单位
Refresh_interval = 20

#设置汇率货币，默认为 1, 如修改人民币，可修改 为 Currency = '人民币'  Exchange_rate = 6.9448
Currency = "美元"
Exchange_rate = 1

# Currency = '人民币'
# Exchange_rate = 6.9448
