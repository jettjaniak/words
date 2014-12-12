# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141208_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='code',
            field=models.CharField(default='en', max_length=2),
            preserve_default=False,
        ),
    ]
