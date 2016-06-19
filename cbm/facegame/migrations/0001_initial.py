# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scores',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=25)),
                ('score', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('last_played', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
