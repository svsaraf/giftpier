# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-16 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azsearch', '0006_auto_20180601_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='asin',
            field=models.CharField(default=b'<function now at 0x106665488>', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
