# Generated by Django 4.2.4 on 2023-09-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0017_cartmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='pro_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
