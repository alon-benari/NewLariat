# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LariatApp', '0007_auto_20171130_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='eating',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hygiene',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mobility',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='toileting',
        ),
    ]