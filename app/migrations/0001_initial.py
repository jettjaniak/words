# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('language', models.CharField(max_length=100, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('word', models.CharField(max_length=200)),
                ('language', models.ForeignKey(to='app.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=set([('language', 'word')]),
        ),
        migrations.AddField(
            model_name='translation',
            name='lang1',
            field=models.ManyToManyField(related_name='translations1', to='app.Word'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='translation',
            name='lang2',
            field=models.ManyToManyField(related_name='translations2', to='app.Word'),
            preserve_default=True,
        ),
    ]
