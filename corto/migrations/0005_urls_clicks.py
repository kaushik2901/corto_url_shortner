# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corto', '0004_browser_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]