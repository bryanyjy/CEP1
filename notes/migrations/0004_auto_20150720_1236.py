# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='content',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='food',
            name='content',
        ),
        migrations.AddField(
            model_name='food',
            name='count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='restaurants',
            field=models.ManyToManyField(to='notes.Restaurant', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
