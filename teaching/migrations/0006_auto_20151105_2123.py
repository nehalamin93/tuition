# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0005_auto_20151105_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_location',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='language',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='qualification',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='temp_address',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='signature_pic',
            field=models.ImageField(default=None, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teaching_level',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='varification_doc1',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='verification_doc2',
            field=models.CharField(default=None, max_length=128),
            preserve_default=True,
        ),
    ]
