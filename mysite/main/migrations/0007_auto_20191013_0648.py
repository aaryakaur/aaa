# Generated by Django 2.2.6 on 2019-10-13 01:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191013_0411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Property'},
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 6, 48, 3, 281078), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flood', models.CharField(max_length=200)),
                ('earthquake', models.CharField(max_length=200)),
                ('property_location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Property', verbose_name='area')),
            ],
            options={
                'verbose_name_plural': 'Property',
            },
        ),
    ]
