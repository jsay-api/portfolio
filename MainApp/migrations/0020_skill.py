# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0019_auto_20160824_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100, verbose_name='Skill name')),
                ('img', models.URLField(verbose_name='Image')),
                ('col', models.CharField(max_length=10, verbose_name='Column: left/right')),
            ],
        ),
    ]
