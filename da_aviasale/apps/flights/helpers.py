# -*- coding: utf-8 -*- #
"""
    Created on 08.07.15 by fashust
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging
import datetime

from django.db.models import F, IntegerField, Sum, DecimalField

from .models import Flight


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


logging.getLogger(__file__)

VALUES_LIST = (
    'dispatch__name', 'arrival__name', 'code_name',
    'total_cost', 'date', 'cost', 'id'
)


class SearchWrapper(object):
    """
        flight search wrapper
    """
    def __init__(self, **kwargs):
        """
            init
        """
        days_delta = 1
        self.dispatch = kwargs.get('dispatch')
        self.arrival = kwargs.get('arrival')
        self.date = (
            kwargs.get('date') - datetime.timedelta(days=days_delta),
            kwargs.get('date') + datetime.timedelta(days=days_delta)
        )
        self.places = kwargs.get('places')
        self.cost = kwargs.get('cost')

    def search(self):
        """
            search for flights
        """
        flights = Flight.objects.select_related(
            'dispatch__name', 'arrival__name'
        ).filter(
            date__range=self.date,
            dispatch=self.dispatch,
            arrival=self.arrival
        ).annotate(
            available_seats=Sum(
                (F('total_seats') - F('reserved_seats')),
                output_field=IntegerField()
            )
        ).filter(available_seats__gte=self.places)
        if self.cost:
            flights = flights.filter(cost__lte=self.cost)
        return flights.annotate(
            total_cost=(F('cost') * self.places),
        ).values(
            *VALUES_LIST
        )