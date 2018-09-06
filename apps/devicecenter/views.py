# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import mj_communication

# Create your views here.

def open_door(request):
    dev = mj_communication.WGPaketShort()
    dev.send_data()

    return render(request, 'test.html')

