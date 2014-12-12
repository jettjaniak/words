# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141208_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='language',
            new_name='name',
        ),
    ]
