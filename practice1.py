"""Write a program which will find all such numbers which are divisible by 7 but are
not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""

l = []
for i in range(2000,3201):
	if (i%7==0) and (i%5!=0):
		l.append(str(i))
#       l.append(i) 

#print(l)
print(','.join(l))


"""Write a program which can compute the factorial of a given numbers:"""

def fact(x):
    if x==0 or x==1:
        return 1
    return x * fact(x - 1)

x = int(input())
print(fact(x))
    
"""With a given integral number n, write a program to generate a dictionary
 that contains (i, i*i) such that is an integral number between 1 and n 
 (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:"""

n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i**2
    
print(d)


"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math

c = 50
h = 30
val = []
items = [x for x in input().split(',')]
for d in items:
    val.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    
print(','.join(val))

"""Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"""

inp_str = input()
dimensions = [int(x) for x in inp_str.split(',')]
rowDim = dimensions[0]
colDim = dimensions[1]
multiList = [[0 for col in range(colDim)] for row in range(rowDim)]

for row in range(rowDim):
    for col in range(colDim):
        multiList[row][col] = row*col

print(multiList)


"""Write a program which accepts a sequence of comma separated 4 digit 
binary numbers as its input and then check whether they are divisible 
by 5 or not. The numbers that are divisible by 5 are to be printed in 
a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010"""

val = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p,2)
    if intp % 5 == 0:
        val.append(p)
        
print(','.join(val))



























