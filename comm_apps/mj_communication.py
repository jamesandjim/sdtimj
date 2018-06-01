#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-28 15:11
# @Author  : James
# @Site    : 
# @File    : mj_communication.py
# @Software: PyCharm
from socket import *

#数据报及其操作方法
#4、接收服务器发送回的数据包
#5、对接收到的数据包进行解析

#定义软件使用的固定的常量
Type = 0x17
ControllerPort = 60000
SpecialFlag = 0x55AAAA55
WGPacketSize = 64

# 定义UDP数据包
udp_data = bytearray(WGPacketSize)
udp_data[0] = 0x17


def send_data(udp_data, ADDR):
    udp_cli_socket = socket(AF_INET, SOCK_DGRAM)

    try:
        udp_cli_socket.sendto(udp_data, ADDR)
        rec_data, ADDR = udp_cli_socket.recvfrom(64)

        if len(rec_data) == WGPacketSize:
            if (int(bytearray(rec_data[0])) == udp_data[0] and int(bytearray(rec_data[1])) == udp_data[1]):
                x = 'ok'
                return x
            else:
                x = 't'
                return x
        else:
            x = 'no'
            return x

    except Exception, e:
        pass


    udp_cli_socket.close()












#对收到的数据进行解析













