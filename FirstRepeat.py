'''
Given an array of integers arr[], The task is to find the index of first repeating element in it
i.e. the element that occurs more than once and whose index of the first occurrence is the smallest.

Input: arr[] = {10, 5, 3, 4, 3, 5, 6}

Output: 5'''

def firstrepeat(n):
    k=[]
    r=[]
    for i in range(len(n)):
        if n[i] not in k:
            k.append(n[i])
        else:
            r.append(i)
            exit
    return(r)
            
            
    
def firstRepeatElemant(arr):
    l=set()
    repeat=set()
    for i in arr:
        if i in l:
            repeat.add(i)
        else:
            l.add(i)
    if(len(repeat)==0):
        return("No Repeating Element")
    for i in arr:
        if i in repeat:
            return i       
a=list(map(int,input().split()))
print(firstRepeatElemant(a))



'''
10,5,3,4,3,5,6

l= 10,5,3,4
repeat=5,3

'''
