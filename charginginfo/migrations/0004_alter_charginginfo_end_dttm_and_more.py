# Generated by Django 4.1.1 on 2022-12-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charginginfo', '0003_alter_charginginfo_end_dttm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charginginfo',
            name='end_dttm',
            field=models.DateTimeField(verbose_name='충전완료일시'),
        ),
        migrations.AlterField(
            model_name='charginginfo',
            name='start_dttm',
            field=models.DateTimeField(verbose_name='충전시작일시'),
        ),
    ]
