'''
3Q)
Given an array of positive integers, find 2 elements such that their xor: a ^ b is maximum.

Input Format
First line of input contains N: the size of the array. The second line contains N integers - the elements of the array.

Constraints
2 <= N <= 103
0 <= A[i] <= 106

Output Format
For each test case, print the value of the maximum xor, separated by new line.

Sample Input 0
3
12 15 9
Sample Output 0
6
Explanation 0
You can form the following xor pairs:
12^15 = 3, 12^9 = 5, 15^9 = 6 : max = 6'''

def xormax(n,l):
    
    max=0
    for i in range(n-1):
        for j in range(i+1,n):
            k=l[i]^l[j]
            if max<k:
                max=k
    return max

n=int(input())
l=list(map(int,input().split()))
print(xormax(n,l))
