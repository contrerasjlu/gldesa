# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galaxy_operator', '0003_auto_20150830_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth', models.DateField()),
                ('ssoTax', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(default=b'Atlanta', max_length=50)),
                ('state', models.CharField(default=b'GA', max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'NC', b'North Caroline'), (b'SC', b'South Caroline'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'ND', b'North Dakota'), (b'SD', b'South Dakota'), (b'DE', b'Delaware'), (b'FL', b'Florida'), (b'GA', b'Giorgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Luisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NJ', b'New Jersey'), (b'NY', b'New York'), (b'NH', b'New Hampshire'), (b'NW', b'New Mexico'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island '), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('zip', models.IntegerField()),
                ('telephone', models.CharField(max_length=20)),
                ('bank', models.CharField(max_length=20)),
                ('bankAcct', models.CharField(max_length=50)),
                ('email', models.EmailField(default=b'@', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('share', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recla', models.DateField()),
                ('agent', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('refered', models.ForeignKey(to='galaxy_operator.AgentDetail')),
            ],
        ),
        migrations.AddField(
            model_name='agentdetail',
            name='level',
            field=models.ForeignKey(to='galaxy_operator.level'),
        ),
        migrations.AddField(
            model_name='agentdetail',
            name='prevAgent',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
