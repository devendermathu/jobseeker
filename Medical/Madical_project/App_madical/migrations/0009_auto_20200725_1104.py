# Generated by Django 2.2.11 on 2020-07-25 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_madical', '0008_auto_20200725_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instock',
            name='N_data',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 25, 11, 4, 24, 752773), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='M_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 25, 11, 4, 24, 752362), null=True),
        ),
    ]
