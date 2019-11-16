# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:10:31 2019

@author: lenovo
"""

def iq_test(numbers):
    num = map(int, numbers.split(" "))
    odds = [o for o in num if o % 2 != 0]
    print(odds)
    evens = [e for e in num if e % 2 == 0]
    print(evens)
    return odds[0] if len(evens) > len(odds) else evens[0]