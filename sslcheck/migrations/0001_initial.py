# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-17 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='checktask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('domain', models.CharField(max_length=100)),
                ('module', models.CharField(max_length=100)),
                ('frequency', models.IntegerField()),
                ('lastcheck', models.IntegerField(default=0)),
            ],
        ),
    ]
