#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import functools

def ignore_exception_decorator(func):
    """どんなエラーも無視してしまうデコレータ"""
    @functools.wraps(func)
    def ignore_exception(*args, **kargs):
        try:
            return func(*args, **kargs)
        except:
            pass
    return ignore_exception
