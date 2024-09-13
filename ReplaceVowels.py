'''
Create a function that replaces all the vowels in a string with a specified character.
replaceVowels("the aardvark", '#') ➞ "th# ##rdv#rk"
replaceVowels("minnie mouse", '?') ➞ "m?nn?? m??s?"
replaceVowels("shakespeare", '*') ➞ "sh*k*sp**r*"
'''

def replaceVowels(k,l):
    result=""
    for i in k:
        if (i.lower() in ('a','e','i','o','u')):
            result+=l
        else:
            result+=i
    return result
    
k=input()
l=input()
p=replaceVowels(k,l)
print(p)

''' def replaceVowels(k,l):
    v="aeiouAEIOU"
    for i in v:
        k=k.replace(i,l)
    return k
    
m=input()
n=input()
p=replaceVowels(m,n)
print(p)
'''
