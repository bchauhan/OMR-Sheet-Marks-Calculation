# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMRCheck', '0015_auto_20170822_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='Username',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]