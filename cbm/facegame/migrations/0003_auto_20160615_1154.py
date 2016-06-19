# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facegame', '0002_level1_level2_level3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level1',
            name='label',
        ),
        migrations.RemoveField(
            model_name='level2',
            name='label',
        ),
        migrations.RemoveField(
            model_name='level3',
            name='label',
        ),
    ]
