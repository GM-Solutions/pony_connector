# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-16 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0003_auto_20200128_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceheader',
            name='close_flag',
            field=models.IntegerField(blank=True, db_column='CFLAG', null=True),
        ),
    ]
