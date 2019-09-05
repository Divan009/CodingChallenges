def maxSubArray(self, nums: List[int]) -> int:
# Kadane Algorithm
# If we know the max subarray ending at position B(i), then what is 
# the max subarray ending at position B(i+1)?
# Max subarray ending at position i+1 includes max subarray ending
# at position i
# B(i+1) = max( A(i+1), A(i+1) + B(i) ) 


# max_current is the maximum subaaray which ends at the current index
# max_global is the ultimate subarray
    max_current = max_global = nums[0]
    #for i from 1 to len(nums) - 1
    for i in nums[1:]:
        max_current = max(i, max_current + i) 
        max_global = max(max_global, max_current)
    return max_global