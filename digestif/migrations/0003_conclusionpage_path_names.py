# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 23:19
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('digestif', '0002_remove_conclusionpage_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='conclusionpage',
            name='path_names',
            field=jsonfield.fields.JSONField(default='NULL'),
        ),
    ]