# Generated by Django 4.2.4 on 2023-09-09 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0008_rename_img_cartmodel_card'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cartmodel',
        ),
    ]