# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_navigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='nav_seq',
            field=models.PositiveSmallIntegerField(default=1, unique=True, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe5\xba\x8f\xe5\x8f\xb7'),
            preserve_default=False,
        ),
    ]
