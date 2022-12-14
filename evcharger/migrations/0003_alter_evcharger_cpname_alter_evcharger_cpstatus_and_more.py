# Generated by Django 4.1.1 on 2022-11-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evcharger', '0002_remove_evcharger_connector_id_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evcharger',
            name='cpname',
            field=models.CharField(max_length=64, verbose_name='충전소이름'),
        ),
        migrations.AlterField(
            model_name='evcharger',
            name='cpstatus',
            field=models.CharField(max_length=64, verbose_name='충전기상태'),
        ),
        migrations.AlterField(
            model_name='evcharger',
            name='cpversion',
            field=models.CharField(max_length=64, verbose_name='충전기버전'),
        ),
    ]
