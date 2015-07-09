# -*- coding: utf-8 -*- #
"""
    Created on 09.07.15 by fashust
    orders admin
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from .models import Order


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class OrdersAdmin(admin.ModelAdmin):
    """
        orders model admin
    """
    list_display = (
        'date', 'flight', 'name',
        'cost', 'total_cost'
    )


admin.site.register(Order, OrdersAdmin)