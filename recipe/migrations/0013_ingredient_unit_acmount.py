# Generated by Django 2.1 on 2018-09-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_auto_20180905_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit_acmount',
            field=models.IntegerField(default=0),
        ),
    ]
