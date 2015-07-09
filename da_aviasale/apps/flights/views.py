# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging

from django.views.generic import View
from django.core.cache import cache
from django.conf import settings

from da_aviasale.utils import JSONRequestResponseMixin

from .forms import FlightsSearchForm
from .helpers import SearchWrapper


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


logging.getLogger(__file__)


class SearchViewHandler(View, JSONRequestResponseMixin):
    """
        search handler
    """
    def __init__(self, **kwargs):
        """
            init
        """
        super(SearchViewHandler, self).__init__(**kwargs)
        self.response = {
            'status': True,
            'data': {},
            'errors': {}
        }

    def post(self, request, *args, **kwargs):
        """
            get handler
        """
        search_form = FlightsSearchForm(request.POST)
        if not search_form.is_valid():
            self.response.update({
                'status': False,
                'errors': self.parse_json(search_form.errors.as_json())
            })
            return self.render_to_response(self.response)
        self.response.update({
            'data': {
                'results': list(
                    SearchWrapper(**search_form.cleaned_data).search()
                ),
                'user_data': {'places': search_form.cleaned_data['places']}
            }
        })
        return self.render_to_response(self.response)


class LockFlightViewHandler(View, JSONRequestResponseMixin):
    """
        lock flight for order
    """
    def __init__(self, **kwargs):
        """
            init
        """
        super(LockFlightViewHandler, self).__init__(**kwargs)
        self.response = {
            'status': True,
            'data': {},
            'errors': {}
        }

    def get(self, request, *args, **kwargs):
        """
            get method handler
        """
        lock = request.GET.get('lock', None)
        if not lock or not request.is_ajax():
            self.response.update({
                'status': False,
                'errors': 'lock is required'
            })
            return self.render_to_response(self.response)
        if (
                not lock.isdigit() or
                int(lock) not in SearchWrapper.get_flights_ids()
        ):
            self.response.update({
                'status': False,
                'errors': 'nothing to lock'
            })
            return self.render_to_response(self.response)
        cache.set(lock, True, settings.LOCK_TIMEOUT)
        self.response.update({
            'data': int(lock)
        })
        return self.render_to_response(self.response)