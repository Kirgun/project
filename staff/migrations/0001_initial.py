# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('lust_name', models.CharField(max_length=40)),
                ('age', models.IntegerField(max_length=3)),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=7)),
                ('salary', models.IntegerField()),
                ('position', models.CharField(max_length=50)),
            ],
        ),
    ]
