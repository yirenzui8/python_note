#!/usr/bin/env python
#_*_conding:utf-8_*_
import threading
import time


def pr(i):
    time.sleep(2)
    print i
for b in range(5):
    a = threading.Thread(target=pr,args=(b,))
    a.start()