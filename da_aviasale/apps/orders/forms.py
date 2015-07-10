# -*- coding: utf-8 -*- #
"""
    Created on 10.07.15 by fashust
    orders forms
"""
from __future__ import absolute_import, print_function, unicode_literals

from decimal import Decimal

from django import forms

from ..flights.models import Flight


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class FlightOrderForm(forms.Form):
    """
        flight order form
    """
    flight = forms.ModelChoiceField(
        queryset=Flight.objects.all(),
        required=True,
        to_field_name='id'
    )
    name = forms.CharField(
        max_length=128,
        required=True
    )
    places = forms.IntegerField(
        min_value=1,
        required=True
    )
    cost = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=True
    )
    total_cost = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=True
    )

    def clean(self):
        """
            clean form data
        """
        cleaned_data = super(FlightOrderForm, self).clean()
        flight = cleaned_data.get('flight', None)
        places = cleaned_data.get('places', None)
        cost = cleaned_data.get('cost', None)
        total_cost = cleaned_data.get('total_cost', None)
        if (
                flight and
                places and
                (
                    not flight.available_seats or
                    flight.available_seats < places
                )
        ):
            self.add_error('flight', 'no available places')
        if flight and not flight.is_locked:
            self.add_error('flight', 'flight is not locked')
        if flight and cost and flight.cost != cost:
            self.add_error('cost', 'cost did not match flight cost')
        if (
                flight and places and total_cost and
                (flight.cost * places).quantize(Decimal('0.00')) !=
                total_cost.quantize(Decimal('0.00'))
        ):
            self.add_error('total_cost', 'total cost mist match')