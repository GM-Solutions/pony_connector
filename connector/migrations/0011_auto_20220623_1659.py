# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-06-23 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0010_auto_20211113_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='adjust_quantity',
            field=models.FloatField(blank=True, db_column='ADJQTY', null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='all_quantity',
            field=models.FloatField(blank=True, db_column='ALLQTY', null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='hold_quantity',
            field=models.FloatField(blank=True, db_column='HOQTY', null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order_quantity',
            field=models.FloatField(db_column='ORDQTY'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='sent_quantity',
            field=models.FloatField(blank=True, db_column='SENTQTY', null=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='ware_house_qty',
            field=models.FloatField(blank=True, db_column='WH_TRFQTY', null=True),
        ),
        migrations.AlterField(
            model_name='productmaster',
            name='size',
            field=models.CharField(db_column='PSIZE', max_length=20),
        ),
    ]
