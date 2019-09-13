#!/usr/bin/env python
# -*- coding:  utf-8 -*-

import errno
import contextlib
import ctypes
import signal
import threading

class TimeoutException(IOError):
    errno = errno.EINTR

@contextlib.contextmanager
def time_limit_with_sigalrm(timeout_secs):
    """
    timeout_secs秒後にタイムアウトを発生させるコンテキストマネージャ。
    タイムアウトするとIOError(errno.EINTR)が発生する。
    
    Notes
    -----
    TimeoutExceptionはfinally節の後処理中でも問答無用で発生するので、関数time_limitの使用を推奨する。
   利用できる環境はUnixのみ &  シグナルは常にメインスレッドで処理される
    """
    orig_sialrm_handler = signal.getsignal(signal.SIGALRM)
    def raise_excetion(signum, frame):
        raise TimeoutException
    
    signal.signal(signal.SIGALRM, raise_excetion)
    signal.alarm(timeout_secs)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, orig_sialrm_handler)

@contextlib.contextmanager
def time_limit_with_thread(timeout_secs):
    """
    timeout_secs秒後にタイムアウトを発生させるコンテキストマネージャ。
    タイムアウトするとTimeoutExceptionが発生する。
    
    Notes
    -----
    TimeoutExceptionはfinally節の後処理中でも問答無用で発生するので、関数time_limitの使用を推奨する。
    """
    thread_id = ctypes.c_long(threading.get_ident())
    def raise_exception():
        modified_thread_state_nums = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(TimeoutException))
        if modified_thread_state_nums == 0:
            raise ValueError('Invalid thread id. thread_id:{}'.format(thread_id))
        elif modified_thread_state_nums > 1:
            # 通常このパスを通ることはないが、念のため保留中のExceptionをクリアしておく
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            raise SystemError('PyThreadState_SetAsyncExc failure.')
    
    timer = threading.Timer(timeout_secs, raise_exception)
    timer.setDaemon(True)
    timer.start()
    try:
        yield
    finally:
        timer.cancel()
        timer.join()

@contextlib.contextmanager
def time_limit(timeout_secs):
    """
    timeout_secs秒後にタイムアウトを発生させるコンテキストマネージャ。
    タイムアウトするとtimeout_eventがセットされる。
    """
    timeout_event = threading.Event()
    timer = threading.Timer(timeout_secs, lambda : timeout_event.set())
    timer.setDaemon(True)
    timer.start()
    try:
        yield timeout_event
    finally:
        timer.cancel()
        timer.join()