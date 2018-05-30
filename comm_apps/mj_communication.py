#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-28 15:11
# @Author  : James
# @Site    : 
# @File    : mj_communication.py
# @Software: PyCharm
from socket import *


class WGPacketShort():
    global WGPacketSize, Type, ControllerPort, SpecialFlag, functionID, buff, iDevSn, data
    WGPacketSize = 64
    Type = 0x17
    ControllerPort = 60000
    SpecialFlag = 0x55AAAA55
    functionID = 0xff
    buff = []
    iDevSn = 0
    data = [56]

    def to_byte(self, buflen):
        if buflen == WGPacketSize:
            buff[0] = Type
            buff[1] = functionID
            buff[4:8] = iDevSn
            buff[8:65] = data

            return buff

    def run(self, ip, port):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(ip, port)

        s.sendto(buff)






