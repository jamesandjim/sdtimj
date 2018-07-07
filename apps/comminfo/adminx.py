#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-06 13:47
# @Author  : James
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin

from .models import Nation, Device_type, Sys_model



class NationAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class Device_typeAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class Sys_modelAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


xadmin.site.register(Nation, NationAdmin)
xadmin.site.register(Device_type, Device_typeAdmin)
xadmin.site.register(Sys_model, Sys_modelAdmin)

