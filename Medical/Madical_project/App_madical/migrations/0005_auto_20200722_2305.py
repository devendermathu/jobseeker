# Generated by Django 2.2.11 on 2020-07-22 23:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_madical', '0004_auto_20200722_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instock',
            name='N_data',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='M_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
