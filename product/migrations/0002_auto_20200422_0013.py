# Generated by Django 3.0.2 on 2020-04-22 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 0, 13, 51, 826782)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 0, 13, 51, 827463)),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 0, 13, 51, 827483)),
        ),
    ]
