# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
"""
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import patterns, url

from .views import IndexViewHandler


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


urlpatterns = patterns(
    'da_aviasale.apps.index',
    url(r'^$', IndexViewHandler.as_view(), name='index-page')
)