def BubbleSort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(n-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    return a

a=list(map(int,input().split()))
print(BubbleSort(a))
