# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-21 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMRCheck', '0007_auto_20170821_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omrsubmitmodel',
            name='omrsheet',
            field=models.ImageField(upload_to=b''),
        ),
    ]
