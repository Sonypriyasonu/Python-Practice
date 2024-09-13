def fibo(n):
    a=0
    b=1
    l=[0,1]
    c=0
    if n==0 or n==1:
        return 0
    else:
        t=a+b
        while b<n:
            t=a+b
            if(t<n):
                l.append(t)
            a=b
            b=t
        return l
n=int(input())
print(fibo(n))
