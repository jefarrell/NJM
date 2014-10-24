# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', stdimage.models.StdImageField(upload_to=b'%Y/%m/%d', blank=True)),
                ('date', models.DateTimeField(default=datetime.date(2014, 10, 16), auto_now=True)),
                ('description', models.TextField(max_length=20000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(default=b'', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('userID', models.CharField(default=b'', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
