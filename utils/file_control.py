#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import os
import contextlib

@contextlib.contextmanager
def pushd(path):
    """作業ディレクトリをpathに移動し、作業後は元ディレクトリに戻るコンテキストマネージャ"""
    olddir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(olddir)

