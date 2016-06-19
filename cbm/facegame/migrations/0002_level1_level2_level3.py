# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facegame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='level1',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('label', models.DecimalField(decimal_places=0, max_digits=1)),
                ('photo', models.ImageField(upload_to='cbmimages/level1_images')),
            ],
        ),
        migrations.CreateModel(
            name='level2',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('label', models.DecimalField(decimal_places=0, max_digits=1)),
                ('photo', models.ImageField(upload_to='cbmimages/level2_images')),
            ],
        ),
        migrations.CreateModel(
            name='level3',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('label', models.DecimalField(decimal_places=0, max_digits=1)),
                ('photo', models.ImageField(upload_to='cbmimages/level3_images')),
            ],
        ),
    ]
