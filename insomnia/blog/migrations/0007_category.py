# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150423_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cate_name', models.CharField(max_length=120, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
