# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(default=0, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GenericVars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=17)),
                ('description', models.TextField()),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=250)),
                ('address', models.TextField(max_length=250)),
                ('zipCode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='menuOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OutType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=250)),
                ('value', models.IntegerField()),
                ('tracking', models.CharField(max_length=17)),
                ('client', models.ForeignKey(default=1, to='galaxy_operator.Client')),
            ],
        ),
        migrations.CreateModel(
            name='PackageDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PackagesRoute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PackageTypeAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('attributeType', models.CharField(max_length=1, choices=[(b'I', b'Integer'), (b'V', b'Varchar')])),
                ('packageType', models.ForeignKey(to='galaxy_operator.PackageType')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=250)),
                ('stateType', models.CharField(max_length=2, choices=[(b'IN', b'Recibed'), (b'OT', b'Delivered')])),
                ('location', models.ForeignKey(to='galaxy_operator.Location')),
            ],
        ),
        migrations.CreateModel(
            name='StateAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('out_type', models.ForeignKey(to='galaxy_operator.OutType')),
                ('state', models.ForeignKey(to='galaxy_operator.State')),
            ],
        ),
        migrations.CreateModel(
            name='StateAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('attributeType', models.CharField(max_length=1, choices=[(b'I', b'Integer'), (b'V', b'Varchar')])),
                ('state', models.ForeignKey(to='galaxy_operator.State')),
            ],
        ),
        migrations.CreateModel(
            name='StateDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=250)),
                ('attribute', models.ForeignKey(to='galaxy_operator.StateAttribute')),
                ('package', models.ForeignKey(to='galaxy_operator.Package')),
            ],
        ),
        migrations.AddField(
            model_name='packagesroute',
            name='route',
            field=models.ForeignKey(to='galaxy_operator.Route'),
        ),
        migrations.AddField(
            model_name='packagesroute',
            name='state',
            field=models.ForeignKey(to='galaxy_operator.State'),
        ),
        migrations.AddField(
            model_name='packagedetail',
            name='attribute',
            field=models.ForeignKey(to='galaxy_operator.PackageTypeAttribute'),
        ),
        migrations.AddField(
            model_name='packagedetail',
            name='package',
            field=models.ForeignKey(to='galaxy_operator.Package'),
        ),
        migrations.AddField(
            model_name='package',
            name='currentState',
            field=models.ForeignKey(to='galaxy_operator.State'),
        ),
        migrations.AddField(
            model_name='package',
            name='operator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='package',
            name='origin',
            field=models.ForeignKey(to='galaxy_operator.Location'),
        ),
        migrations.AddField(
            model_name='package',
            name='packageType',
            field=models.ForeignKey(to='galaxy_operator.PackageType'),
        ),
        migrations.AddField(
            model_name='package',
            name='route',
            field=models.ForeignKey(to='galaxy_operator.Route'),
        ),
    ]
