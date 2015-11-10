# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0004_auto_20151105_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='per_address',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
    ]
