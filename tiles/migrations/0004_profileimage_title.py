# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0003_auto_20141017_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileimage',
            name='title',
            field=models.TextField(default='Temp Title', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
