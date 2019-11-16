# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:43:03 2019

@author: lenovo
"""

i = "aaabcccd"
i = "aaa"
i = "b"
i = "aaabbccdeee"

def compress_str(string):
    res = ""
    count = 1
    
    if len(string) <= 1:
        res += string[0]+str(count)
        return res
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            res += string[i] + str(count)
            count = 1
    res += string[i+1] + str(count)
    
        
    if len(string) >= len(res):
        return res
    else:
        return string