# -*- coding: utf-8 -*- #
"""
    Created on 09.07.15 by fashust
    orders urls
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import patterns, url

from .views import OrderViewHandler


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


urlpatterns = patterns(
    'da_aviasale.apps.orders',
    url('^$', OrderViewHandler.as_view(), name='order'),
)