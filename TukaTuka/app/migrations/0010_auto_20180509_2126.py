# Generated by Django 2.0.3 on 2018-05-09 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180508_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='user',
        ),
        migrations.DeleteModel(
            name='Merchant',
        ),
    ]
