# Generated by Django 2.0.5 on 2018-06-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180524_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='category1',
            field=models.IntegerField(choices=[(1, 'ПП'), (2, 'ПНД'), (3, 'ПВД'), (4, 'Стрейч'), (5, 'ПЭТ'), (6, 'Другое')], default=0),
        ),
        migrations.AddField(
            model_name='ad',
            name='category2',
            field=models.IntegerField(choices=[(1, 'Гранула ПП'), (2, 'Гранула ПНД'), (3, 'Гранула ПВД'), (4, 'Гранула стрейч'), (5, 'Другое')], default=0),
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.IntegerField(choices=[(1, 'Купить вторичное сырье на переработку'), (2, 'Купить переработанное сырье'), (3, 'Продать вторичное сырье на переработку'), (4, 'Продать переработанное сырье')], default=0),
        ),
    ]
