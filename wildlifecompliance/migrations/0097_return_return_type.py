# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-23 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0096_auto_20181023_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='return',
            name='return_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.ReturnType'),
        ),
    ]
