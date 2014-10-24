# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0004_profileimage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='date',
            field=models.DateTimeField(default=datetime.date(2014, 10, 18), auto_now=True),
        ),
    ]
