#!/usr/bin/env python
# -*- coding:  utf-8 -*-

from utils.logging import findCaller

def call(back_depth=0):
    print(findCaller(back_depth=back_depth))

def call_depth1(back_depth=1):
    call(back_depth=back_depth)

def call_depth2(back_depth=2):
    call_depth1(back_depth=back_depth)

if __name__ == '__main__':
    call()
    call_depth1()
    call_depth2()