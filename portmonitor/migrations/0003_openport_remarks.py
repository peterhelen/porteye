# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-18 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portmonitor', '0002_remove_openport_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='openport',
            name='remarks',
            field=models.TextField(blank=True, default=''),
        ),
    ]
