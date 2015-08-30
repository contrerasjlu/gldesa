# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_operator', '0002_auto_20150830_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(default=b'@', max_length=254),
        ),
        migrations.AlterField(
            model_name='state',
            name='stateType',
            field=models.CharField(max_length=3, choices=[(b'IN', b'Recibed'), (b'OUT', b'Delivered')]),
        ),
    ]
