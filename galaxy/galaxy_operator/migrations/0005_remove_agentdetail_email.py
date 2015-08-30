# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_operator', '0004_auto_20150830_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentdetail',
            name='email',
        ),
    ]
