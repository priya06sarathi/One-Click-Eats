# Generated by Django 4.2.4 on 2023-09-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0025_alter_cartmodel_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='quantity',
        ),
    ]
