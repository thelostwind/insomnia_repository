# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_navigation_nav_seq'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Navigation',
            new_name='Navigator',
        ),
    ]
