l=list(map(int,input().split()))
def garden(l):
    s=0
    k=0
    m=min(l)
    n=len(l)
    for i in range(n):
        k+=l[i]-m
        if s<k:
            s=k 
    return s
print(garden(l))     
