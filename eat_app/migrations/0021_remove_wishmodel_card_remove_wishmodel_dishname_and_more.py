# Generated by Django 4.2.4 on 2023-09-20 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0020_profilmodel_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishmodel',
            name='card',
        ),
        migrations.RemoveField(
            model_name='wishmodel',
            name='dishname',
        ),
        migrations.RemoveField(
            model_name='wishmodel',
            name='no_per',
        ),
        migrations.RemoveField(
            model_name='wishmodel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='wishmodel',
            name='uid',
        ),
    ]