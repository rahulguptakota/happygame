# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facegame', '0003_auto_20160615_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='level1',
            name='label',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='level2',
            name='label',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='level3',
            name='label',
            field=models.BooleanField(default=0),
        ),
    ]
