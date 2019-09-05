#Code Wars

def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if (i % 2 > 0):
            odds.append[i]
        if (i % 2 == 0):
            evens.append[i]
        
    print("Even: ", evens)
    print("Odd: ", odds)
    
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]

find_outlier([2, 4, 6, 8, 10, 3])

#Sol 2:-
def find_outlier2(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]