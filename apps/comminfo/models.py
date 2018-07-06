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

