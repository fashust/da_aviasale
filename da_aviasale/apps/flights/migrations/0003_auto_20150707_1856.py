# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'places',
            },
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival',
            field=models.ForeignKey(related_name='arrives_to', to='flights.Place'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='dispatch',
            field=models.ForeignKey(related_name='dispatch_from', to='flights.Place'),
        ),
    ]
