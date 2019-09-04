#!/usr/bin/env python
# -*- coding:  utf-8 -*-

from utils.logging import findCaller

def call(wrapper_depth=0):
    print(findCaller(wrapper_depth=wrapper_depth))

def call_depth1(wrapper_depth=1):
    call(wrapper_depth=wrapper_depth)

def call_depth2(wrapper_depth=2):
    call_depth1(wrapper_depth=wrapper_depth)

if __name__ == '__main__':
    call()
    call_depth1()
    call_depth2()