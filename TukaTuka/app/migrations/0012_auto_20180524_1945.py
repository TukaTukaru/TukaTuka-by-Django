# Generated by Django 2.0.5 on 2018-05-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_mail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mail',
            options={'verbose_name': 'email', 'verbose_name_plural': 'emails'},
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.IntegerField(choices=[(1, 'Гранула ПП'), (2, 'Гранула ПНД'), (3, 'Гранула ПВД'), (4, 'Гранула стрейч'), (5, 'Другое')], default=0),
        ),
    ]
