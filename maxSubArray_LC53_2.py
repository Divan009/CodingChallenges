# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 00:13:11 2019

@author: lenovo
"""

data = [1,2,3,-9,5,7,-99,2,8]
#data = [1,2,3,4,5]

# part 1
# =============================================================================
# for x in range(len(data)+1):
#     for j in range(len(data)+1):
#         print(data[x:j])
# =============================================================================


#Brute Force method        
def max_arr(input_arr):
    global_max = 0
    indicies = []
    for i in range(len(data)+1):
        for j in range(len(data)+1):
            curr_sum = sum(data[i:j])
            # print(curr_sum, data[i:j])
            if curr_sum > global_max:
                global_max = curr_sum
                indicies.append((i,j-1))
    return global_max, indicies.pop()

max_arr(data)