# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
import os


from django.shortcuts import render

from sdtimj.settings import BASE_DIR
# Create your views here.

def DeviceOperation(request):
    ex = os.path.join(BASE_DIR, "libs/wg/IPCon2015_V2.17.exe")



  