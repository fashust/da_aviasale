# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging

from django.views.generic import View
from django.http import HttpResponse

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
