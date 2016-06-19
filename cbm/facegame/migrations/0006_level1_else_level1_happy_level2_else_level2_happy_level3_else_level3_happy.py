# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facegame', '0005_auto_20160615_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='level1_else',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('elsephoto', models.ImageField(blank=True, upload_to='cbmimages/level1_images/else', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='level1_happy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('happyphoto', models.ImageField(upload_to='cbmimages/level1_images/happy')),
            ],
        ),
        migrations.CreateModel(
            name='level2_else',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('elsephoto', models.ImageField(blank=True, upload_to='cbmimages/level2_images/else', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='level2_happy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('happyphoto', models.ImageField(upload_to='cbmimages/level2_images/happy')),
            ],
        ),
        migrations.CreateModel(
            name='level3_else',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('elsephoto', models.ImageField(blank=True, upload_to='cbmimages/level3_images/else', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='level3_happy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('happyphoto', models.ImageField(upload_to='cbmimages/level3_images/happy')),
            ],
        ),
    ]
