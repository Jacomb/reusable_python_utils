#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import os
from utils.logging import logput as _logput
from utils.logging import init_logging
from utils.file_control import pushd

MYLOGGER = 'sample.pushd'
def logput(msg, **kargs):
    return _logput(msg, logger=MYLOGGER, wrapper_depth=1, **kargs)

def main():
    logput(os.getcwd())
    with pushd('../utils'):
        logput(os.getcwd())
    logput(os.getcwd())

if __name__ == '__main__':
    init_logging()
    main()