# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_food_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='restaurants',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='food',
            field=models.ManyToManyField(to='notes.Food'),
            preserve_default=True,
        ),
    ]
