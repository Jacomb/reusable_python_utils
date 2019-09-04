#!/usr/bin/env python
# -*- coding:  utf-8 -*-

from utils.logging import logput as _logput
from utils.logging import logging_fcuntion_decorator as _logging_fcuntion_decorator
from utils.logging import DEBUG

# 引数logger, wrapper_depthをこのスクリプト用に固定した関数を作る。
MYLOGGER = 'sample.logput'
def logput(msg, **kargs):
    return _logput(msg, logger=MYLOGGER, wrapper_depth=1, **kargs)

def logging_fcuntion_decorator(**kargs):
    return _logging_fcuntion_decorator(logger=MYLOGGER, **kargs)

# 実際の使い方
@logging_fcuntion_decorator(level=DEBUG)
def plus(a, b):
    return a + b

@logging_fcuntion_decorator(level=DEBUG)
def minus(a, b):
    return a - b

@logging_fcuntion_decorator(level=DEBUG)
def main1():
    x, y = 20, 10
    logput('x:{}, y:{}'.format(x, y))
    return plus(x, y), minus(a=x, b=y)

@logging_fcuntion_decorator(level=DEBUG)
def main2():
    raise Exception

if __name__ == '__main__':
    try:
        # plusやminus等の関数を実行する様を可視化
        main1()
        
        # エラーが発生した場合もTracebackをログ出力
        main2()
        
    except:
        pass
