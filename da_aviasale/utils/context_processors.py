# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
    simple context processors
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging

from ..apps.flights.forms import FlightsSearchForm


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


logging.getLogger(__file__)


def forms_context(request):
    """
        inject forms to context
    """
    return {
        'search_form': FlightsSearchForm()
    }