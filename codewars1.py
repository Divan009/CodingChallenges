# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:33:33 2019

@author: lenovo
"""
nameList = ([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])


def nameL(names):
    n = [name['name'] for name in nameList]
    
    if len(n) <= 1:
        return ''.join(n)
    else:
        lastTwo = ' & '.join(n[-2:])
        first = [i + ',' for i in n[:-2]]
        first.append(lastTwo)
        return ''.join(first)
    

