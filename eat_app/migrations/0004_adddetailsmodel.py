# Generated by Django 4.2.4 on 2023-08-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_app', '0003_profilmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='adddetailsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
