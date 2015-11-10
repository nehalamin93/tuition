# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0003_auto_20151105_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_location',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='language',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='per_address',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(default=999999999),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='qualification',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='standard',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='temp_address',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
