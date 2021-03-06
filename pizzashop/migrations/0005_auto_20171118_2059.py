# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0004_auto_20171118_1851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pizzashop.Customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='pizzashop.OrderItem', to='pizzashop.Item', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='count',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
