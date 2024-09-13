'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''

def findmedian(l,l1):
    i=j=0
    a=[]     
    while i<len(l) and j<len(l1):
        if l[i]<l1[j]:
            a+=[l[i]]
            i+=1
        else:
            a+=[l1[j]]
            j+=1
    while(i<len(l)):
        a+=[l[i]]
        i=i+1
    while(j<len(l1)):
        a+=[l1[j]]
        j=j+1
    n=len(a)
    if n%2==0:
        m=(a[n//2-1] + a[n//2])/2
    else:
        m=a[n//2]   
    return m

l=list(map(int,input().split()))
l1=list(map(int,input().split()))
print(findmedian(l,l1))
