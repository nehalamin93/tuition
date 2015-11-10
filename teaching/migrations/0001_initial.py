# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('per_address', models.CharField(max_length=128)),
                ('temp_address', models.CharField(max_length=128)),
                ('class_location', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('class_days', models.CharField(max_length=128)),
                ('available_days', models.CharField(max_length=128)),
                ('qualification', models.CharField(max_length=128)),
                ('specialisation', models.CharField(max_length=128)),
                ('experience', models.CharField(max_length=128)),
                ('shift_type', models.CharField(max_length=128)),
                ('teaching_level', models.CharField(max_length=128)),
                ('rating', models.CharField(max_length=128)),
                ('profile_pic', models.CharField(max_length=128)),
                ('signature_pic', models.CharField(max_length=128)),
                ('varification_doc1', models.CharField(max_length=128)),
                ('verification_doc2', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
