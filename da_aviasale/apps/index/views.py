# -*- coding: utf-8 -*- #
"""
    Created on 07.07.15 by fashust
    index views
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging

from django.views.generic import TemplateView


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


logging.getLogger(__file__)


class IndexViewHandler(TemplateView):
    """
        index page handler
    """
    template_name = 'index.html'