# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171113_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authorq',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_dateq',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_dateq',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='textq',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titleq',
            new_name='title',
        ),
    ]
