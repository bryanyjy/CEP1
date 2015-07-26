# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20150720_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='about',
            new_name='address',
        ),
    ]
