# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0002_dish_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('CR', 'Создан'), ('NCF', 'Не подтвержден'), ('CF', 'Подтвержден'), ('CBC', 'Отменен заказчиком'), ('CBO', 'Отклонен заказчиком'), ('CM', 'Выполнен'), ('FL', 'Провален')], default='CR', max_length=3)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pizzashop.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashop.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashop.Order')),
            ],
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='pizzashop.OrderItem', to='pizzashop.Item'),
        ),
    ]