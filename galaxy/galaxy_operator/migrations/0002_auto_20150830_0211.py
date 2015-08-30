# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_operator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(default=b'Atlanta', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.CharField(default=b'USA', max_length=3),
        ),
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.CharField(default=b'GA', max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'NC', b'North Caroline'), (b'SC', b'South Caroline'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'ND', b'North Dakota'), (b'SD', b'South Dakota'), (b'DE', b'Delaware'), (b'FL', b'Florida'), (b'GA', b'Giorgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Luisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NJ', b'New Jersey'), (b'NY', b'New York'), (b'NH', b'New Hampshire'), (b'NW', b'New Mexico'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island '), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')]),
        ),
    ]
