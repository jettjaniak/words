# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(blank=True, to='app.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='translation',
            name='lang1',
        ),
        migrations.RemoveField(
            model_name='translation',
            name='lang2',
        ),
        migrations.AddField(
            model_name='translation',
            name='categories',
            field=models.ManyToManyField(to='app.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='translation',
            name='words',
            field=models.ManyToManyField(related_name='translations', to='app.Word'),
            preserve_default=True,
        ),
    ]
