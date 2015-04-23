# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150423_1345'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Navigator',
            new_name='Navigation',
        ),
    ]
