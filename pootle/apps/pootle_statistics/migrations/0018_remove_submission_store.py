# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_statistics', '0017_drop_reject_suggestion_subs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='store',
        ),
    ]
