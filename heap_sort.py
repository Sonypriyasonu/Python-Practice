def maxheap(a,n,i):
    max=i
    l=2*i+1
    r=2*i+2
    if l<n and a[l]>a[max]:
        max=l
    if r<n and a[r]>a[max]:
        max=r
    if max!=i:
        a[i],a[max]=a[max],a[i]
        maxheap(a,n,max)

def heap_sort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1):
        maxheap(a,n,i)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        maxheap(a,i,0)
    return a
        
a=list(map(int,input().split()))
print(heap_sort(a)) 
