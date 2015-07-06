# -*- coding: utf-8 -*- #
"""
    Created on 06.07.15 by fashust
    flights models
"""
from __future__ import absolute_import, print_function, unicode_literals

from decimal import Decimal

from django.db import models


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class Flight(models.Model):
    """
        flights model
    """
    code_name = models.CharField(
        max_length=8,
        blank=False,
        null=False
    )
    date = models.DateField(
        null=False,
        blank=False
    )
    dispatch = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )
    arrival = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )
    total_seats = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False
    )
    reserved_seats = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal('0.00').quantize(Decimal('0.00'))
    )

    class Meta:
        """
            model meta
        """
        app_label = 'flights'
        db_table = 'flight'

    def __unicode__(self):
        """
            unicode
        """
        return '{}: {} -> {}'.format(
            self.code_name,
            self.dispatch,
            self.arrival
        )