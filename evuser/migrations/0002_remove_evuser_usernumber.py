# Generated by Django 4.1.1 on 2022-10-24 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evuser',
            name='usernumber',
        ),
    ]