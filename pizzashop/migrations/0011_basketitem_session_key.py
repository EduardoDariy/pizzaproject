# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0010_auto_20171203_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='session_key',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
