# Generated by Django 4.2.4 on 2023-09-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0018_cartmodel_pro_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]