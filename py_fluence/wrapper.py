#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Wrapper(object):
    def __init__(self, *args, **kwargs):
        super(Wrapper, self).__init__(*args, **kwargs)


class DatabaseWrapper(Wrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

# vim: filetype=python
