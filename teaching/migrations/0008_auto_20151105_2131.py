# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0007_auto_20151105_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rating',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
