# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150415_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nav_title', models.CharField(unique=True, max_length=20, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe5\x90\x8d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
