def mergeSort(a):
    n=len(a)
    if n>1:
        m=n//2
        l=a[:m]
        r=a[m:]
        mergeSort(l)
        mergeSort(r)
        i=j=k=0
        
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
            
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
            
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1
    return a
        
a=list(map(int,input().split()))
print(mergeSort(a))
