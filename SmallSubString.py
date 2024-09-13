'''
4)Given 2 strings A and B, find the smallest substring of B having all the characters of A, in any order.
Input Format
First line of input 2 space separated strings - A and B.
Constraints
1 <= size(A), size(B) <= 100
General Constraints
'a' <= A[i],B[i] <= 'z'
Output Format
print the length of the smallest substring of B having all the characters of A, separated by newline. If no such substring found, print -1.

Sample Input 0
fkqyu frqkzkruqmfqyuzlkyg
Sample Output 0
7
Sample Input 1
bloets lwbcrsfothplxseplrtbshbtstjloxsf
Sample Output 1
13
Sample Input 2
onmwvytbytn uqhmfjaqtgngcwkuzyamnerphfmw
Sample Output 2
-1'''

a="bloets"
b="lwbcrsfothplxseplrtbshbtstjloxsf"
n=len(b)
p=""
g=[]
min=n
for i in range(n):
    for j in range(i,n):
        p=b[i:j+1]
        c=0
        for k in a:
            if k not in p:
                c=1
                break  
                         
        if c==0:
            if len(p)<min:
                min=len(p)
                g=[i,j]
if len(b)==min:
    print("-1")
else:
    print(b[g[0]:g[1]+1])
    print(min)
