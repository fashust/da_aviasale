# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import patterns, url

from .views import SearchViewHandler, LockFlightViewHandler


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


urlpatterns = patterns(
    'da_aviasale.apps.flights',
    url(r'^flights/?', SearchViewHandler.as_view(), name='flights-search'),
    url(r'^lock/?', LockFlightViewHandler.as_view(), name='flights-lock'),
)