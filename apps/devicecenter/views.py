# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from mj_communication import WGPaketShort

# Create your views here.

def open_door(request):
    dev = WGPaketShort('192.168.0.99', 123300755, 0x40)
    # dev.ip = '192.168.0.99'
    # dev.func_id = 0x40
    # dev.dev_sn = 123300755
    dev.door_id = 1

    ret = dev.send_data()

    return render(request, 'test.html', {'x': ret})

