# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_operator', '0005_remove_agentdetail_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuoption',
            name='imgClass',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menuoption',
            name='url',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
