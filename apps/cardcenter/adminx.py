#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-06 09:18
# @Author  : James
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm

import xadmin

from .models import Organization, Personnel, Card_for_personnel


class OrganizationAdmin(object):
    list_display = ['org_name']
    list_filter = ['org_name']
    search_fields = ['org_name']


class PersonnelAdmin(object):
    list_display = ['name', 'nation', 'gender', 'organization', 'phone', 'address', 'ID_Card_NO']
    list_filter = ['name', 'nation', 'gender', 'organization', 'phone', 'address', 'ID_Card_NO']
    search_fields = ['name', 'nation', 'gender', 'organization', 'phone', 'address', 'ID_Card_NO']
    #list_editable = ['name', 'nation']
    #refresh_times = (3, 5)

    # data_charts = {
    #     u'图形分布' : {'title': u'占比表', 'x-field': 'name', 'y-field': 'phone'}
    # }


class Card_for_personnelAdmin(object):
    list_display = ['personnel', 'card_no']
    list_filter = ['personnel', 'card_no']
    search_fields = ['personnel', 'card_no']


xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(Personnel, PersonnelAdmin)
xadmin.site.register(Card_for_personnel, Card_for_personnelAdmin)