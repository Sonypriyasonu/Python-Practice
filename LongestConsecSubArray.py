'''
Write a Java program to check if a sub-array is formed by consecutive integers 
from a given array of integers.
Example:
Input :
nums = { 2, 5, 0, 2, 1, 4, 3, 6, 1, 0 }
Output:
The largest sub-array is [1, 7]
Elements of the sub-array: 5 0 2 1 4 3 6'''

'''def consec(a):
    min1=min(a)
    l=len(a)
    for i in range(len(a)):
        if min1 not in a:
            return 0
        min1=min1+1
    return 1'''
def consc(a):
    m1=min(a)
    m2=max(a)
    n1=((m1-1)*m1)/2
    n2=(m2*(m2+1))/2
    k=n2-n1
    k1=sum(a)
    if k==k1:
        return 1
    
def solve(a):
    n=len(a)
    m=0
    k=[]
    for i in range(n):
        for j in range(i+1,n):
            s=a[i:j+1]
            f=consc(s)
            if(f==1):
                if(m<len(s)):
                    m=len(s)
                    k=[i,j]
                  
    if m==0: 
        return("no concecutives")      
    #return k
    else:
        p=k[0]
        y=k[1]
        return a[p:y+1]
l=list(map(int,input().split()))
a=solve(l)
print(a)
'''for i in range(a[0],a[1]+1):
    print(l[i])'''
