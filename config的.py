#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version: v1.0
@author:Colin
@file: config.py
@time: 3/9/2020/4:19 PM
"""
# 原油价格的低价购入提醒，可设置多个，设置一个举例：Minimum_reminder = [27]
#设置多个举例： Minimum_reminder = [27, 28.5, 29]
Minimum_reminder = [27]
#原油价格高价卖出提醒
Highest_reminder = [32]
#设置监控类型，0代表监控低价，1代表监控高价
Reminder_type = 0

#设置发送邮件的邮箱，需登录邮箱开启smtp服务，密码非邮箱登录密码，是开启smtp服务后给到的密码
Host_server = 'smtp.qq.com'
Email = 'example@qq.com'
Email_passwod = 'password'

#设置接受邮箱,添加多个用逗号隔开
Receiver = ['example@qq.com']

#原油价格刷新时间间隔，以秒为单位
Refresh_interval = 20

#设置汇率货币，默认为 1, 如修改人民币，可修改 为 Currency = '人民币'  Exchange_rate = 6.9448
Currency = "美元"
Exchange_rate = 1

# Currency = '人民币'
# Exchange_rate = 6.9448


