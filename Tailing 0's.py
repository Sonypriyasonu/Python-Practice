'''2)Count the number of trailing 0s in factorial of a given number.

Input Format
First line of input containing an integer N.
Constraints
1 <= N <= 10^15
Output Format
print the number of trailing 0s in N!, separated by new line.
Sample Input 0
5!
Sample Output 0
1
Explanation 0
5! = 120 [Trailing zeros=1]
Sample Input 1
20!
Sample Output 1
4
Explanation 1
20! = 2432902008176640000 [Trailing zeros=4]
'''

def  fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        k=1
        while n>1:
            k*=n
            n-=1
        return k

def tailing (n):
    k=str(n)
    c=0
    for i in range(len(k)-1,-1,-1):
        if k[i]=='0':
            c+=1
        else:
            break
    return c
       
n=int(input())
k=fac(n)
print(k)
print(tailing(k))
