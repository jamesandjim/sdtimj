#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-06 09:18
# @Author  : James
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm

import xadmin

from .models import Organization, Personnel


class OrganizationAdmin(object):
    list_display = ['org_name']
    list_filter = ['org_name']
    search_fields = ['org_name']


class PersonnelAdmin(object):
    list_display = ['name', 'gender', 'organization']
    list_filter = ['name', 'gender']
    search_fields = ['name', 'gender']


xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(Personnel, PersonnelAdmin)