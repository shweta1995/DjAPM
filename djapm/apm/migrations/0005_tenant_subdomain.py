# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-30 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apm', '0004_auto_20161128_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='subdomain',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
