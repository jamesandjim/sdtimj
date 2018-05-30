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

class WGPacketShort():

    global WGPacketSize, Type, ControllerPort, SpecialFlag, functionID, buff, iDevSn, data, ADDR #1、定义需发送的数据包的内容
    WGPacketSize = 64
    Type = 0x17
    ControllerPort = 60000
    SpecialFlag = 0x55AAAA55
    functionID = 0xff
    buff = []
    iDevSn = 0
    data = [56]
    HOST = '192.168.0.100'
    PORT = 60000
    ADDR = (HOST, PORT)

    def to_byte(self, str, buflen):                                                         #2、对需发送的内容进行格式化
        if buflen == WGPacketSize:
            buff[0] = Type
            buff[1] = functionID
            buff[4:8] = iDevSn
            buff[8:65] = data

            return buff

    def run(self, buff, ADDR):                                                                #3、基于UDP协议发送数据包
        udp_cli_socket = socket(AF_INET, SOCK_DGRAM)

        while True:
            try:
                udp_cli_socket.sendto(buff, ADDR)
                data, ADDR = udp_cli_socket.recvfrom(64)

                if not data:
                    break
                if len(data) == WGPacketSize:
                    if data[0] == Type and data[1] == functionID:
                        return data

            except Exception,  e:
                pass

        udp_cli_socket.close()


#对收到的数据进行解析
   












