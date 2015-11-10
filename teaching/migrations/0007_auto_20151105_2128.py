# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0006_auto_20151105_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='qualification',
            field=models.CharField(default=None, max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(default=None, max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='rating',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='signature_pic',
            field=models.ImageField(default=None, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teaching_level',
            field=models.CharField(default=None, max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='varification_doc1',
            field=models.CharField(default=None, max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='verification_doc2',
            field=models.CharField(default=None, max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
