# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0005_auto_20171118_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pizzashop.Customer', verbose_name='Клиент'),
        ),
    ]