# -*- coding: utf-8 -*- #
"""
    Created on 09.07.15 by fashust
    orders views
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging

from django.views.generic import View

from da_aviasale.utils import JSONRequestResponseMixin

from .forms import FlightOrderForm
from .models import Order


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


logging.getLogger(__file__)


class OrderViewHandler(View, JSONRequestResponseMixin):
    """
        make order view handler
    """
    def __init__(self, **kwargs):
        """
            init
        """
        super(OrderViewHandler, self).__init__(**kwargs)
        self.response = {
            'status': True,
            'data': {},
            'errors': {}
        }

    def post(self, request, *args, **kwargs):
        """
            post method handler
        """
        order_form = FlightOrderForm(request.POST)
        if not order_form.is_valid():
            self.response.update({
                'status': False,
                'errors': self.parse_json(order_form.errors.as_json())
            })
            return self.render_to_response(self.response)
        Order.objects.create(**order_form.cleaned_data)
        return self.render_to_response(self.response)