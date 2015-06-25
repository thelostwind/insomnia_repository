# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(db_column=b'post_category', default=1, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='blog.Category'),
            preserve_default=False,
        ),
    ]
