'''
Find all the permutations in the given array 
arr=[1,2,3]
output => [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]'''

def permute(l):
    n=len(l)
    if n==0:
        return [[]]
    elif n==1:
        return l
    else:
        r=[[]]
        for i in l:   #1,2,3
            p=[]
            for j in r:              
                for k in range(len(j)+1):                 
                    p.append(j[:k]+[i]+j[k:])
            r=p
        #return sorted(r) 
        return ["".join(m) for m in sorted(r)]
        
        
#arr=[1,2,3]
s="abc"
#print(permute(arr))
k=permute(list(s))
print(k)
for i in k:
    print(i)

#second max
k=[2,44,7,8,9,455,455,66,55]
a=set(k)
b=max(a)
a.remove(b)
print(max(a))

a='dabdcafsg'
b='ddcf'
def samc(a,b):
    k=0
    for i in range(len(a)):
        k=0
        for j in range(i,len(a)):
            if k<len(b) and b[k]==a[j]:
                k=k+1
            if(k==len(b)):
                return 1
    return 0
            

    '''for i in b:
        if i in a:
            k+=i
            if k in a:
                l.append(a.find(k))'''
    return k
print(samc(a,b))
                
        
def coun(a,b):
    k={}
    k1={}
    for i in a:
        k[i]=0
    for i in a:
        k[i]+=1
    for i in b:
        k1[i]=0
    for i in b:
        k1[i]+=1 
    for key,value in k1.items():
        if key in k:
            if k[key]!=value:
                return "FALSE"
        else:
            return "FALSE"
    return "TRUE"
        

print(coun(a,b))
def permutations(lst):
    if len(lst) == 0:
        return [[]]  # Base case: empty list has one permutation, an empty list

    result = []
    for i in range(len(lst)):
        # Extract the current element
        current = lst[i]
        
        # Generate permutations of the remaining list
        remaining = lst[:i] + lst[i+1:]
        sub_permutations = permutations(remaining)
        
        # Append current element to each permutation of the remaining list
        for perm in sub_permutations:
            result.append([current] + perm)
    
    return result

# Example usage:
my_list = [1, 2, 3]
print(permutations(my_list))

s="foo"
t="egg"
def gooo(s,t):
    s1=set()
    for i in s:
        s1.add(i)
    l1=[]
    l2=[]
    for i in s1:
        k=[]
        for j in range(0,len(s)):
            if(i==s[j]):
                k.append(j)
        l1.append(k)
    s2=set()
    for i in t:
        s2.add(i)
    for i in s2:
        k=[]
        for j in range(0,len(t)):
            if(i==t[j]):
                k.append(j)
        l2.append(k)
    l1.sort()
    l2.sort()
    return l1==l2
print(gooo(s,t))

s=['hhhiiittt', 'hhit','hit']
def hit(s):
    k=0
    for i in s:
        if len(i)>k:
            k=len(i)
    return k
print(hit(s))
    
'''converting number to binary and then check count and then taking 2 power of'''
x=[1,2,3,4,5]
v=[]
z=[]
 
for i in x:
    v.append(bin(i)[2:])
print(v)
for i in v:
    c=0
    for j in i:
        c+=1
    z.append(2**c)
print(z)
w=[]
w2=[]
for i in x:
    w.append(bin(i)[2:])   
w2.append(2**len(w))
print(z)

def is_palindrome(n):
    return str(n) == str(n)[::-1]
 
def closest_symmetric_number(num):
    if is_palindrome(num):
        return num
   
    lower = num - 1
    upper = num + 1
   
    while True:
        if is_palindrome(lower):
            return lower
        elif is_palindrome(upper):
            return upper
        lower -= 1
        upper += 1
 
# Example usage:
number = 123
closest_symmetric = closest_symmetric_number(number)
print("Closest symmetric number to", number, "is", closest_symmetric)
 
'''closest symmetric'''
n=1221
x=str(n)
w=len(x)
mid=w//2
y=[]
if w%2==0:
    y=x[:mid]+x[mid-1::-1]
else:
    y=x[:mid+1]+x[mid-1::-1]
print(y)
z=int(bin(int(y))[2:])
print(z)

#longest subarray

s1='adventure'
s2='future'
a=[]
m=s=0
for i in range(0,len(s1)):
    for j in range(i+1,len(s1)+1):
        if s1[i:j] in s2:
            a.append(s1[i:j])
for i in a:
    if len(i)>m:
        m=len(i)
        k=i
print(k)
for i in k:
    s+=ord(i)
print(s)
 
n=100000
s=''
x=str(n)
comma=(len(x)//2)-1
c=0
if n<=999:
    print(0)
else:
    while comma>=1:
        s=('99'*(comma-1)+'999')
        c+=(int(x)-int(s))*comma
        x=s
        comma-=1
    print(c)
#minimum power
import math
n=108
pm1=40
pm2=8
m_only=math.ceil((n/100))*pm1
m_in=(n//100)*pm1
rem=n%100
t=math.ceil(rem/4)*pm2
x=m_in+t
print(min(x,m_only))
 
import math
n=['hello','ccbb','aaeiou']
x=[]
for i in n:
    c=0
    for j in i:
        if j.lower()  not in ['a','e','i','o','u']:
            c+=1
    x.append(math.factorial(c))
print(max(x))
#MINIMUM BADNESS
x='RRW'
c=0
if 'R' not in x and 'B' not in x:
    print(0)
else:
    for i in range(len(x)):
 
        if x[0]=='W':
            if x[i]!='W':
                x=x.replace(x[0],x[i],1)
        elif x[i]=='W':
            x=x.replace(x[i],x[i-1],1)
for i in range(1,len(x)):
    if x[i-1]!=x[i]:
        c+=1
print(c)
 
#max product
n=[11,1,2,8,10,11,15,7]
z=[]
m=0
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)-1):
        if n[i]+n[j]==18:
            if n[i]*n[j]>m:
                m=n[i]*n[j]
                z.append(n[i])
                z.append(n[j])
x=z[::-1]
print(x)
 
#olivias garden
x=[-1,-2,-2,9]
z=min(x)
s=0
for i in range(len(x)):
    s+=x[i]-z
print(s)
