# Generated by Django 4.2.4 on 2023-09-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0023_remove_wishmodel_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='confirmmodel',
        ),
        migrations.AlterField(
            model_name='cartmodel',
            name='card',
            field=models.FileField(upload_to=''),
        ),
    ]
