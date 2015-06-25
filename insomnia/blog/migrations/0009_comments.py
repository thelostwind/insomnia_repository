# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('comment_author', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85')),
                ('comment_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('comment_content', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('comment_post', models.ForeignKey(db_column=b'comment_post', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
