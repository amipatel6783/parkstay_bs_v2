# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-01 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0053_assessment_assessor_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='licence_activity_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.WildlifeLicenceActivityType'),
        ),
    ]
