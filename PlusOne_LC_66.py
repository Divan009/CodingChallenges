# -*- coding: utf-8 -*-


# =============================================================================
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# =============================================================================


data = [1,2,9]
data = [9]

# =============================================================================
# def plusOne(input_data):
#     if input_data[-1] == 9:
#         input_data[-2] = input_data[-2]+1
#     for i in range(len(input_data)):  
#         if i == len(input_data)-1:
#             input_data[i] = input_data[i]+1
#     return input_data
# =============================================================================

def pluss(list):   
    # Converting integer list to string list 
    # and joining the list using join() 
    # [1,2,3] -> 123 == int
    res = int("".join(map(str, list))) 
    res += 1
    returnList = [int(x) for x in str(res)] 
    return returnList
    