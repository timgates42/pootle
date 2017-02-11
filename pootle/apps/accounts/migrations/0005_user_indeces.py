# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-23 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_allow_null_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(db_index=True, default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Superuser Status'),
        ),
    ]