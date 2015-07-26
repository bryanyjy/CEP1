# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20150720_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='info',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
