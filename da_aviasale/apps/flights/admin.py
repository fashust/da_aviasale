# -*- coding: utf-8 -*- #
"""
    Created on 06.07.15 by fashust
    flights admin
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from .models import Flight


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class FlightAdmin(admin.ModelAdmin):
    """
        flights model admin
    """
    list_display = (
        'date', 'code_name', 'dispatch', 'arrival', 'total_seats',
        'reserved_seats', 'cost'
    )


admin.site.register(Flight, FlightAdmin)