# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ctypes import *
import os

from django.shortcuts import render

from sdtimj.settings import BASE_DIR
# Create your views here.

class DeviceOperation():
    dll = cdll.LoadLibrary(os.path.join(BASE_DIR, 'libs/wg/n3kAdrtC.dll'))

  