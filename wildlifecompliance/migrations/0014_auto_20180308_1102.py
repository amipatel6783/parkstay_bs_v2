# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-08 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0013_organisationrequest_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationcontact',
            name='user_role',
            field=models.CharField(choices=[('organisation_admin', 'Organisation Admin'), ('organisation_user', 'Organisation User'), ('auth_agent', 'Authorised Agent')], default='organisation_user', max_length=40, verbose_name='Role'),
        ),
    ]
