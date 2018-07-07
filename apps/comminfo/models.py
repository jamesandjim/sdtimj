# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#
class Nation(models.Model):
    name = models.CharField(verbose_name=u'民族', max_length=20, default=u'汉')

    class Meta:
        verbose_name = u'民族信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Device_type(models.Model):
    name = models.CharField(verbose_name=u'设备类型名称', max_length=50, default=u'门禁设备')

    class Meta:
        verbose_name = u'设备类型管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Sys_model(models.Model):
    name = models.CharField(verbose_name=u'系统模块名称', max_length=50, default=u'门禁系统')

    class Meta:
        verbose_name = u'系统模块管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name