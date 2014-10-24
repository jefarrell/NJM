# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tile',
        ),
        migrations.AddField(
            model_name='profileimage',
            name='s',
            field=models.SlugField(default='NA'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='date',
            field=models.DateTimeField(default=datetime.date(2014, 10, 17), auto_now=True),
        ),
    ]
