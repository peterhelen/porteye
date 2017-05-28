# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-22 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portmonitor', '0007_ip_remarks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ip_remarks',
        ),
        migrations.RemoveField(
            model_name='ipremarks',
            name='address',
        ),
        migrations.RemoveField(
            model_name='ipremarks',
            name='inserted',
        ),
        migrations.RemoveField(
            model_name='ipremarks',
            name='taskid',
        ),
        migrations.AddField(
            model_name='ipremarks',
            name='business',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name='ipremarks',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ipremarks',
            name='ip_addr',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='ipremarks',
            name='own',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='ipremarks',
            name='remarks',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]
