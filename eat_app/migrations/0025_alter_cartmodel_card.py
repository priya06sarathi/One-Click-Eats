# Generated by Django 4.2.4 on 2023-09-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0024_delete_confirmmodel_alter_cartmodel_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='card',
            field=models.FileField(upload_to='eat_app/static'),
        ),
    ]