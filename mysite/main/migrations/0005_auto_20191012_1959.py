# Generated by Django 2.2.6 on 2019-10-12 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191012_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 19, 59, 7, 346409), verbose_name='date published'),
        ),
    ]