# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_name', models.CharField(max_length=8)),
                ('date', models.DateField()),
                ('dispatch', models.CharField(max_length=128)),
                ('arrival', models.CharField(max_length=128)),
                ('total_seats', models.PositiveSmallIntegerField(default=0)),
                ('reserved_seats', models.PositiveIntegerField(default=0)),
                ('cost', models.DecimalField(default=Decimal('0.00'), max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'flight',
            },
        ),
    ]
