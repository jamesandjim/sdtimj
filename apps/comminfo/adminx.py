#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-06 13:47
# @Author  : James
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin

from .models import Nation



class NationAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


xadmin.site.register(Nation, NationAdmin)
