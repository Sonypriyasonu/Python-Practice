'''
1)Create a function that takes two numbers and a mathematical operator + - / * and will
perform a calculation with the given numbers.
Examples
 
calculator(2, '+', 2) ➞ 4
calculator(2, '*', 2) ➞ 4
calculator(4, '/', 2) ➞ 2
 
Notes
If the input tries to divide by 0, return 0.'''

def calculator(n,s,k):
    if s == '+':
        return n+k
    elif s =='*':
        return n*k
    elif s=="-":
        return n-k
    elif s=="/":
        if k==0:
            return 0
        else:
            return int(n/k)
    
    
n=int(input())
s=input()
k=int(input())
print(calculator(n,s,k))
