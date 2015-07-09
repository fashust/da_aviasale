# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20150707_1856'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('places', models.PositiveIntegerField()),
                ('cost', models.DecimalField(max_digits=6, decimal_places=2)),
                ('total_cost', models.DecimalField(max_digits=12, decimal_places=2)),
                ('flight', models.ForeignKey(to='flights.Flight')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
    ]
