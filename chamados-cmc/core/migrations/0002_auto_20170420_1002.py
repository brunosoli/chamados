# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='id_elotech',
            field=models.IntegerField(unique=True),
        ),
    ]
