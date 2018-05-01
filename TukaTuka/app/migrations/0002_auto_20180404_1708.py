# Generated by Django 2.0.3 on 2018-04-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companys',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='companys',
            name='site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
