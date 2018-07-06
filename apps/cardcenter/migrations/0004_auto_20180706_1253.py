# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardcenter', '0003_personnel_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_for_personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(default='', max_length=10, verbose_name='\u5361\u7247\u7269\u7406\u53f7')),
            ],
            options={
                'verbose_name': '\u4eba\u5458\u53d1\u5361',
                'verbose_name_plural': '\u4eba\u5458\u53d1\u5361',
            },
        ),
        migrations.AddField(
            model_name='personnel',
            name='ID_Card_NO',
            field=models.CharField(default='', max_length=18, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u7801'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='\u4f4f\u5740'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='nation',
            field=models.CharField(default='\u6c49', max_length=10, verbose_name='\u6c11\u65cf'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='phone',
            field=models.CharField(default='', max_length=11, verbose_name='\u7535\u8bdd\u53f7\u7801'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cardcenter.Organization', verbose_name='\u6240\u5c5e\u673a\u6784'),
        ),
        migrations.AddField(
            model_name='card_for_personnel',
            name='personnel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cardcenter.Personnel'),
        ),
    ]
