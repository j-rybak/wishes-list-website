# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Team member',
                'verbose_name_plural': 'Team member',
            },
        ),
    ]
