'''Largest Gap	
Given an array of integers, return the largest gap between elements of the sorted version of that array.
Here's an illustrative example. Consider the array:
[9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]
... which, after sorting, becomes the array:
[0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]
... so that we now see that the largest gap in the array is the gap of 11 between 9 and 20.	largestGap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]) ➞ 11
// After sorting get [0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]
// Largest gap of 11 between 9 and 20
largestGap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]) ➞ 4
// After sorting get [1, 3, 4, 5, 7, 7, 7, 7, 11, 12, 12, 13, 14]
// Largest gap of 4 between 7 and 11
largestGap([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]) ➞ 2
// After sorting get [1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]
// Largest gap of 2 between 6 and 8'''

def LargestGap(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(n-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    l=[]
    print(a)
    for i in range(n-1):
        l.append(a[i+1]-a[i])
    print(l)
    k=max(l)
    m=[]
    m1=[]
    for i in range(n-1):
        if (a[i+1]-a[i])==k:
            m+=[a[i+1]]
            m1+=[a[i]]     
    return "Largest gap of "+str(k)+" between "+str (m)+ " and "+str(m1)

a=list(map(int,input().split()))
print(LargestGap(a))
