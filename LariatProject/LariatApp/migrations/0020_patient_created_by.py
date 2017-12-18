# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 00:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LariatApp', '0019_remove_patient_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
