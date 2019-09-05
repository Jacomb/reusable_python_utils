#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import logging

logging.basicConfig(format='%(funcName)s >> %(message)s', level=logging.DEBUG)
def logput(msg):
    # ここに何か便利な処理
    logging.debug(msg)

def main():
    logput('mainを開始')
    # ここでmainの処理
    logput('mainを終了')
    
if __name__ == '__main__':
    main()