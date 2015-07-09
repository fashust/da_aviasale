# -*- coding: utf-8 -*- #
"""
    Created on 09.07.15 by fashust
    orders models
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.core.cache import cache
from django.db import models


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class Order(models.Model):
    """
        order model
    """
    date = models.DateField(
        auto_now_add=True
    )
    flight = models.ForeignKey(
        to='flights.Flight',
        to_field='id',
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )
    places = models.PositiveIntegerField(
        blank=False,
        null=False
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    total_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    class Meta:
        """
            model meta
        """
        app_label = 'orders'
        db_table = 'payments'

    def __unicode__(self):
        """
            unicode
        """
        return '{}: {} -> {}, {}'.format(
            self.date,
            self.flight.dispatch.name,
            self.flight.arrival.name,
            self.total_cost
        )

    def save(self, **kwargs):
        """
            save order
        """
        super(Order, self).save(**kwargs)
        self.flight.reserved_seats += self.places
        self.flight.save()
        self.remove_lock()

    def remove_lock(self):
        """
            remove lock from flight
        """
        cache.delete(self.flight.id)