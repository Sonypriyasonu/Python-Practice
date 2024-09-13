'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.'''
def LargeSubArray(a):
    sa=0
    en=0
    sum=0
    max1=0
    for i in range(len(a)):
        sum+=a[i]
        if(max1<sum):
            max1=sum
            en=i
        if(sum<0):
            sum=0
            sa=i+1
    print(max1,sa,en)
        
    #return max1
    return f"The subarray {a[sa:en+1]} has the largest sum {max1}"
'''max1=0
    res_arr=[]
    for i in range(len(a)):
        s=a[i]
        for j in range(i+1,len(a)):
            s=s+a[j]
            if(max1<s):
                max1=s
                res_arr=a[i:j+1]
            print(a[i:j+1])
    print(res_arr)
    return f"The subarray {res_arr} has the largest sum {max1}" '''
            
a=list(map(int,input().split()))
print(LargeSubArray(a))
