# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_operator', '0006_auto_20150830_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuoption',
            name='activeOn',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
