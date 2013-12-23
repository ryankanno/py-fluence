#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Context(object):
    def __init__(self, *args, **kwargs):
        super(Context, self).__init__(*args, **kwargs)


class FileContext(Context):
    def __init__(self, file_path, *args, **kwargs):
        super(FileContext, self).__init__(*args, **kwargs)
        self.file_path = file_path


class Config(FileContext):
    def __init__(self, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)

# vim: filetype=python
