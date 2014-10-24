# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0002_auto_20141017_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileimage',
            old_name='s',
            new_name='slug',
        ),
    ]
