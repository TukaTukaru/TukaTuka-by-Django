# Generated by Django 2.0.3 on 2018-05-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_merchant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='email',
            field=models.EmailField(db_index=True, default='', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
