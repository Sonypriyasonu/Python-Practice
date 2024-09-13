def quickSort(a):
    if len(a)<2:
        return a
    else:
        pivot = a[0]
        left =[i for i in a[1:] if i<pivot]
        right=[i for i in a[1:] if i>=pivot]
        return quickSort(left)+[pivot]+quickSort(right)

a=list(map(int,input().split()))
#a=[7,9,7,5]
print(quickSort(a))
