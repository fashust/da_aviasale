# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
"""
from __future__ import absolute_import, print_function, unicode_literals


from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Place


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class FlightsSearchForm(forms.Form):
    """
        flights search form
    """
    date = forms.DateField(widget=AdminDateWidget, required=True)
    dispatch = forms.ModelChoiceField(
        queryset=Place.objects.all(),
        required=True,
        to_field_name='id'
    )
    arrival = forms.ModelChoiceField(
        queryset=Place.objects.all(),
        required=True,
        to_field_name='id'
    )
    places = forms.IntegerField(
        min_value=1,
        required=True
    )
    cost = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False
    )