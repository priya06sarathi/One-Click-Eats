# Generated by Django 4.2.4 on 2023-09-07 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0006_cartmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='dishname',
        ),
    ]