# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Restaurant',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='title',
            new_name='name',
        ),
    ]
