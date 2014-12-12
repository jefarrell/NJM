# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0005_auto_20141018_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileimage',
            name='weblink',
            field=models.TextField(default='https://www.google.com/', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='date',
            field=models.DateTimeField(default=datetime.date(2014, 12, 10), auto_now=True),
            preserve_default=True,
        ),
    ]
