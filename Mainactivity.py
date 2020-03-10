#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version: v1.0
@author:Colin
@file: Mainactivity.py
@time: 3/9/2020/4:13 PM
"""

from get_crude_data import get_crude_data, monitor_data
from email_server import send_request_mail
import config
sender = config.Email
receiver = config.Receiver
type = config.Reminder_type

if __name__ == "__main__":
    print("="*100)
    print("首次运行，程序将检查邮箱设置，你设置的邮箱为：{0}，接受邮箱为：{1}".format(sender, receiver))
    print("系统将发送一封邮件，请确认收信情况")
    t1, t2 = get_crude_data()
    send_request_mail(t1,t2,"(本次为测试邮件)")
    print("测试通过，程序开始监控")
    print("=" * 100)
    monitor_data(type)








