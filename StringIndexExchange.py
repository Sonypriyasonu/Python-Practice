'''
Create a function that takes both a string and an array of numbers as arguments. 
Rearrange the letters in the string to be in the order specified by the index numbers.
Return the "remixed" string.
Examples
remix("abcd", [0, 3, 1, 2]) ➞ "acdb"
The string you'll be returning will have: "a" at index 0, "b" at index 3, "c" at index 1, "d" at index 2,
because the order of those characters maps to their corresponding numbers in the index array.'''

def remix(s,l):
    j=0
    res=["*"]*len(s)
    print(res)
    for i in l:
        res[i]=s[j]
        j=j+1
    return "".join(res)
    '''k=""
    for i in l:
        k+=s[i]
    return k'''

s="abcd"
l=[0,3,1,2]  
print(remix(s,l))
