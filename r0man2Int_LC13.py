def rom_int(num):
    rom_num = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500, 'M':1000}
    res = 0
    for i,c in enumerate(num):
    	# print(i,c)
    	# for first iteration
    	# i+1 = 0+1
    	# len(num) = if num = XXIV then len(num) = 4
    	# rom_num[c] = X = 10
    	#rom_num[num[i+1]] = num[i+1] = num[0+1] = num[1]
    	# then rom_num[X] = 10
        if (i+1) == len(num) or rom_num[c] >= rom_num[num[i+1]]:
            res += rom_num[c]
#            print(rom_num[c])
        else:
            res -= rom_num[c]
#            print(-rom_num[c])
    return res

#Runtime: 40 ms, faster than 64.83% of Python online submissions for Roman to Integer.
#Memory Usage: 11.7 MB, less than 62.90% of Python online submissions for Roman to Integer.