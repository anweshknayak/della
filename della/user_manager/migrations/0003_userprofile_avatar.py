# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 07:14
from __future__ import unicode_literals

import della.user_manager.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_userprofile_santee'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='../static/img/avatar.jpg', upload_to=della.user_manager.models.avatar_file_name),
        ),
    ]
