# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0011_basketitem_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='session_key',
        ),
    ]
