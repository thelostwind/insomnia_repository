# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('post_title', models.CharField(max_length=120, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('post_timestamp', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('post_content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('user_login', models.CharField(unique=True, max_length=60, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95\xe5\x90\x8d')),
                ('user_passwd', models.CharField(max_length=164, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('user_nickname', models.CharField(max_length=50, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to='blog.User'),
            preserve_default=True,
        ),
    ]
