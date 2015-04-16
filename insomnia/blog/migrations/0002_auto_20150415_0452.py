# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(db_column=b'post_author', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to='blog.User'),
            preserve_default=True,
        ),
    ]
