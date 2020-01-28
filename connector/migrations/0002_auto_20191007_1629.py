# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='ware_house_qty',
            field=models.IntegerField(blank=True, db_column='WH_TRFQTY', null=True),
        ),
        migrations.AlterField(
            model_name='collectiondetails',
            name='dtlid',
            field=models.IntegerField(blank=True, db_column='DTLID', default=0),
        ),
        migrations.AlterField(
            model_name='collectiondetails',
            name='invoice_id',
            field=models.IntegerField(blank=True, db_column='INVID', default=0),
        ),
        migrations.AlterField(
            model_name='collectiondetails',
            name='invoice_no',
            field=models.CharField(db_column='INVNO', default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='collectiondetails',
            name='receipt_number',
            field=models.IntegerField(blank=True, db_column='RECPTNO', default=0),
        ),
        migrations.AlterField(
            model_name='collectiondetails',
            name='rmasid',
            field=models.IntegerField(blank=True, db_column='RMASID', default=0),
        ),
        migrations.AlterField(
            model_name='collectionheader',
            name='receipt_number',
            field=models.IntegerField(blank=True, db_column='RECPTNO', default=0),
        ),
        migrations.AlterField(
            model_name='collectionheader',
            name='rmasid',
            field=models.IntegerField(blank=True, db_column='RMASID', default=0),
        ),
        migrations.AlterField(
            model_name='customermaster',
            name='customer_code',
            field=models.IntegerField(blank=True, db_column='CUSTCODE', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order_number',
            field=models.IntegerField(blank=True, db_column='OPNO', default=0),
        ),
        migrations.AlterField(
            model_name='orderheader',
            name='order_number',
            field=models.IntegerField(blank=True, db_column='OPNO', default=0),
        ),
    ]