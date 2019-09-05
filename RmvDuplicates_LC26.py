
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    i = 0
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1


#Since the parameters are passed in as a reference to the outer_list, and not a copy.
#We can use the mutating list as a methods to change it & have the changes reflected in the outer_list
def rmvDup(t_l):
    print('got',t_l)
    t_l.append(4)
    print('changed to', t_l)
    
outer_list = [1,2,3]

print('before ', outer_list)
rmvDup(outer_list)
print('after ',outer_list)



#since the t_l was passed by value(a copy of the outer_list reference), and we had t_l point to a 
# new list, but theres no way to change where outer list points at

def rmvDupi(t_l):
    print('got',t_l)
    t_l = [3,2,1]
    print('changed to', t_l)
    
outer_list = [1,2,3]

print('before ', outer_list)
rmvDupi(outer_list)
print('after ',outer_list)
