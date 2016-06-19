# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facegame', '0004_auto_20160615_1158'),
    ]

    operations = [
        migrations.DeleteModel(
            name='level1',
        ),
        migrations.DeleteModel(
            name='level2',
        ),
        migrations.DeleteModel(
            name='level3',
        ),
    ]
