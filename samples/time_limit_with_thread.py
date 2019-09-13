#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import time
from utils.logging import logput as _logput
from utils.logging import logging_function_decorator as _logging_function_decorator
from utils.logging import DEBUG, init_logging, LOPT_NO_ARGUMENTS, LOPT_NO_RETUEN_VALUES
from utils.canceler import time_limit_with_thread, TimeoutException

MYLOGGER = 'sample.time_limit'
def logput(msg, **kargs):
    return _logput(msg, logger=MYLOGGER, wrapper_depth=1, **kargs)

def logging_function_decorator(**kargs):
    # 引数と返値は今回確認したい情報ではないので出力しない
    return _logging_function_decorator(logger=MYLOGGER, logput_options=LOPT_NO_ARGUMENTS|LOPT_NO_RETUEN_VALUES, **kargs)

@logging_function_decorator(level=DEBUG)
def main1():
    """タイムアウトしなかった場合"""
    with time_limit_with_thread(3):
        try:
            time.sleep(1)
        except TimeoutException:
            logput('timeout')

@logging_function_decorator(level=DEBUG)
def main2():
    """タイムアウトした場合"""
    with time_limit_with_thread(3):
        try:
            time.sleep(10)
        except TimeoutException:
            logput('timeout')

@logging_function_decorator(level=DEBUG)
def main3():
    """タイムアウトした場合 (sleepを分割)"""
    with time_limit_with_thread(3):
        try:
            for _ in range(10):
                time.sleep(1)
        except TimeoutException:
            logput('timeout')

@logging_function_decorator(level=DEBUG)
def main4():
    """タイムアウトが後処理中に割り込む危険性がある"""
    with time_limit_with_thread(3):
        try:
            time.sleep(1)
        except TimeoutException:
            logput('timeout.')
        finally:
            # 後処理
            logput('post process start.')
            time.sleep(5)
            logput('post process end.')

if __name__ == '__main__':
    init_logging()
    main1()
    main2()
    main3()
    main4()