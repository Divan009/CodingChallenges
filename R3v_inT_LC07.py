# Reverse Integer
class Sol:
    def reverse(self, x):
        # 2^31
        #store new nunber in num
        num = 0
        # a = 123
        # first iter
        # num = 3
        #return absolute value of a number
        a = abs(x)
        
        while(a != 0):
            # a=123 and rem = 3
            temp = a % 10
            # 0 * 10 + 3
            num = num*10 + temp
            # a = 12
            a = int(a/10)
            
        if x > 0 and num < 2147483647:
            return num
        
        elif x < 0 and num <= 2147483647:
            return -num
        
        else:
            return 0

# Runtime: 28 ms, faster than 9.78% of Python online submissions for 
# Reverse Integer.
# Memory Usage: 11.9 MB, less than 5.38% of Python online 
# submissions for Reverse Integer.


#one more solution
def reverse2(x):
    """type x: int
    rtype: int"""
    
    if x >= 0:
        x = int(str(x)[::-1])
    else: 
        x = int(str(-x)[::-1])
    return x if x <= (2**31-1) and x >= -(2**31) else 0