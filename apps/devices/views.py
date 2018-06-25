# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mj_communication import send_data


from django.shortcuts import render
from django.http import HttpResponse

from sdtimj.settings import BASE_DIR
# Create your views here.

def open_door(request):
    udp_data = bytearray(64)
    udp_data[0] = 0x17
    udp_data[1] = 0x40
    udp_data[4] = 0xEC
    udp_data[5] = 0xF1
    udp_data[6] = 0x4E
    udp_data[7] = 0x0D
    udp_data[8] = 0x01

    ADDR = ('192.168.0.200', 60000)

    rec_data = send_data(udp_data, ADDR)

    return HttpResponse(rec_data)

def index(request):
    return render(request, 'form_layouts.html')





  