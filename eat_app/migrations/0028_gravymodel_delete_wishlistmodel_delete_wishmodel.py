# Generated by Django 4.2.4 on 2023-09-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0027_remove_profilmodel_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='gravymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gravyname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('card', models.FileField(upload_to='eat_app/static')),
            ],
        ),
        migrations.DeleteModel(
            name='wishlistmodel',
        ),
        migrations.DeleteModel(
            name='wishmodel',
        ),
    ]
