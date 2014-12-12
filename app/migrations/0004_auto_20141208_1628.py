# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_language_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=2, unique=True),
            preserve_default=True,
        ),
    ]
