#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-04 18:05
# @Author  : James
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = u'SDTI一卡通系统'
    site_footer = u'成都丰盛时代科技有限公司'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
