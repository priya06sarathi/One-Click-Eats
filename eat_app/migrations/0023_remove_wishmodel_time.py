# Generated by Django 4.2.4 on 2023-09-20 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0022_confirmmodel_alter_cartmodel_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishmodel',
            name='time',
        ),
    ]
