# Generated by Django 2.2.11 on 2020-07-24 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_madical', '0006_auto_20200724_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instock',
            name='N_data',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 24, 15, 43, 5, 454916), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='M_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 24, 15, 43, 5, 454441), null=True),
        ),
    ]