# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-28 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apm', '0003_auto_20161128_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='subdomain',
            new_name='user',
        ),
    ]
