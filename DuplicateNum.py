'''
3)Print duplicate elements in the array ?
 
Sample Input :
 
1,2,3,4,2,7,8,8,3
 
Sample Output :
2
3
8
 '''
def dub(n):
    l=[]
    k=[]
    for i in n:
        if i in l:
            k.append(i)
        else:
            l.append(i)
    k.sort()
    for i in k:
        print(i)
       
n=list(map(int,input().split()))
print(dub(n))
