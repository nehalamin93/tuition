# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=1, max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='class_days',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='experience',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='rating',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='signature_pic',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
