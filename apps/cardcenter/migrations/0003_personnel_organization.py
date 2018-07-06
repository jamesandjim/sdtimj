# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardcenter', '0002_personnel'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cardcenter.Organization'),
        ),
    ]