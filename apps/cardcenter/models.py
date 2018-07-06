# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from comminfo.models import Nation

# Create your models here.

#机构
class Organization(models.Model):
    org_name = models.CharField(max_length=100, verbose_name=u'机构名称')

    class Meta:
        verbose_name = u'机构管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.org_name


#用户信息
class Personnel(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=u'人员名称')
    nation = models.ForeignKey(Nation, default=1)
    gender = models.CharField(max_length=6, choices=(('male',u'男'), ('femal',u'女')), verbose_name=u'性别')
    phone = models.CharField(max_length=11, verbose_name=u'电话号码', default='')
    address = models.CharField(max_length=100, verbose_name=u'住址', default='')
    ID_Card_NO = models.CharField(max_length=18, verbose_name=u'身份证号码', default='')

    organization = models.ForeignKey(Organization, default=1, verbose_name=u'所属机构')

    class Meta:
        verbose_name = u'人员信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

#人员发卡
class Card_for_personnel(models.Model):
    personnel = models.ForeignKey(Personnel, null=False, blank=False, verbose_name=u'人员信息')
    card_no = models.CharField(max_length=10, verbose_name=u'卡片物理号', default='')

    class Meta:
        verbose_name = u'人员发卡'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.personnel.name