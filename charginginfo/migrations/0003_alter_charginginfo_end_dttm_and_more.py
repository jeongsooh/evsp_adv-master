# Generated by Django 4.1.1 on 2022-12-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charginginfo', '0002_alter_charginginfo_end_dttm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charginginfo',
            name='end_dttm',
            field=models.CharField(max_length=64, verbose_name='충전완료일시'),
        ),
        migrations.AlterField(
            model_name='charginginfo',
            name='start_dttm',
            field=models.CharField(max_length=64, verbose_name='충전시작일시'),
        ),
    ]
