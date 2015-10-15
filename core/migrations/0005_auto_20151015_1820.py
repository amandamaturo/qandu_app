# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151013_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
        migrations.AddField(
            model_name='question',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
    ]
