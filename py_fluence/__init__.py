#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from collections import namedtuple
version_info = namedtuple('version_info', ('major', 'minor', 'patch'))


VERSION = version_info(0, 0, 2)


__title__ = 'py_fluence'
__version__ = '{0.major}.{0.minor}.{0.patch}'.format(VERSION)
__author__ = 'Ryan Kanno'
__email__ = 'ryankanno@localkinegrinds.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Ryan Kanno'

# vim: filetype=python
