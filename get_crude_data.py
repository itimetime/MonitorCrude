#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version: v1.0
@author:Colin
@file: get_crude_data.py
@time: 3/9/2020/4:56 PM
"""

import config
import requests
import time
from email_server import send_request_mail

curreny = config.Currency

def get_crude_data():
    url = 'https://w.sinajs.cn/etag.php?_=1583740140782&list=hf_CL'
    crude_data = requests.get(url).text
    crude_price = float(crude_data[18:24])
    updata_time = crude_data[92:102] +' ' + crude_data[54:62]
    return  round(crude_price * config.Exchange_rate, 3), updata_time

def monitor_data(type = 0, mini = config.Minimum_reminder, high = config.Highest_reminder):
    hope_price = mini if type == 0 else high
    remind1 = "现在模式为低价购入提醒，你的期望价格为{0}{1}，程序正在运行...".format(hope_price, curreny)
    remind2 = "现在模式为高价抛出提醒，你的期望价格为{0}{1}，程序正在运行...".format(hope_price, curreny)
    print(remind1) if type == 0 else print(remind2)
    while True:
        crude_price, updata_time = get_crude_data()
        if type == 0:
            temp = [i for i in hope_price if crude_price <= i]
        elif type == 1:
            temp = [i for i in hope_price if crude_price >= i]
        else:
            print("设置有误，请检查config.py中的Reminder_type")
            exit()
        if temp == []:
            print("当前原油价格为{0}{1},更新时间{2}".format(crude_price, curreny,  updata_time) +
                  ",不符合期望价格{0}{1}".format(hope_price, curreny))
            print("等待{0}秒将继续刷新...".format(config.Refresh_interval))
            time.sleep(config.Refresh_interval)
            continue
        else:
            arrive_goal = max(temp) if type == 0 else min(temp)
            remark = "已达到你的期望价格{0}{1}".format(arrive_goal, curreny)
            send_request_mail(crude_price, updata_time, remark)
            hope_price.remove(arrive_goal)
            if hope_price == []:break
            else: continue
    print("已达到目标，监控结束")






