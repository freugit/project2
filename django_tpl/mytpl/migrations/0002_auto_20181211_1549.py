# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-11 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytpl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
