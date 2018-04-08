#!/usr/bin/env python
#-*- conding:utf-8 -*-
'''
def generator_function():
    for i in range(10):
        yield i
for item in generator_function():
    print(item)
    '''
'''
def fibon(n):
    a = b =1
    for i in range(n):
        yield a
        a,b = b,a + b
for x in fibon(100):
    print(x)
'''
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
for x in fibon(100000):
    print(x)