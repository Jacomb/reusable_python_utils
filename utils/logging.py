#!/usr/bin/env python
# -*- coding:  utf-8 -*-

"""
This file has copied and modified the following project code:

Logging package for Python

Copyright 2001-2017 by Vinay Sajip. All Rights Reserved.

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation, and that the name of Vinay Sajip
not be used in advertising or publicity pertaining to distribution
of the software without specific, written prior permission.
VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

import os
import sys
import logging

if hasattr(sys, '_getframe'):
    currentframe = lambda:sys._getframe(0)
else:
    def currentframe():
        try:
            raise Exception
        except Exception:
            return sys.exc_info()[2].tb_frame.f_back

_srcfile = os.path.normcase(currentframe.__code__.co_filename)
def findCaller(srcfiles=[_srcfile], back_depth=0):
    """
    呼出元関数の情報を取得する。
    
    Parameters
    ----------
    srcfiles: list
        srcfilesで定義されたファイルリストよりも上位フレームを呼出元とする。
    back_depth: int
        追加でフレームをいくつ遡るかを指定する。
    """
    f = currentframe().f_back
    
    # srcfilesまで遡る
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename in srcfiles:
            f = f.f_back
            continue
        else:
            break
    else:
        return "(Unknown file)", 0, "(Unknown function)"
    
    # back_depthだけ更に遡る
    for _ in range(back_depth):
        f = f.f_back
        if hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
        else:
            return "(Unknown file)", 0, "(Unknown function)"
    
    return filename, f.f_lineno, co.co_name
