# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
    mixins
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging
import json
from decimal import Decimal, getcontext
import datetime

from django.http import HttpResponse


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'
__all__ = (
    'JSONRequestResponseMixin',
)


logging.getLogger(__file__)


def defaults(val):
    """
        json encoder
    """
    if isinstance(val, Decimal):
        return str(val)
    if isinstance(val, datetime.date):
        return val.strftime('%d/%m/%Y')
    return val


class JSONRequestResponseMixin(object):
    """
        json http response mixin
    """
    def render_to_response(self, content, **kwargs):
        """
            render json respnse
        """
        return self.get_json_response(content, **kwargs)

    @staticmethod
    def get_json_response(content, **kwargs):
        """
        Construct an `HttpResponse` object.
        """
        return HttpResponse(
            json.dumps(
                content,
                encoding='utf-8',
                default=defaults
            ),
            content_type='application/json',
            **kwargs
        )

    def parse_json(self, data):
        """
            django forms errors wrapper
        """
        return json.loads(data)