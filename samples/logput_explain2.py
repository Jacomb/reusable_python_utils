#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import logging
from utils.logging import findCaller

logging.basicConfig(format='%(message)s', level=logging.DEBUG)
def logput(msg):
    funcName = findCaller(wrapper_depth=1)[2]
    logging.debug('{} >> {}'.format(funcName, msg))

def main():
    logput('mainを開始')
    # ここでmainの処理
    logput('mainを終了')
    
if __name__ == '__main__':
    main()