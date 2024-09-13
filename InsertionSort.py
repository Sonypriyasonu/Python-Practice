def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        print("i iter",i)
        while a[j-1]>a[j] and j>0:
            a[j-1],a[j]=a[j],a[j-1]
            j-=1
            print("j iter",j)
            
    return a

a=list(map(int,input().split()))
print(insertionSort(a))
