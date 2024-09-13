'''
Given a string, return a sorted array of words formed from the first three letters, then the next three letters, shifting by only one.
Examples

threeLetterCollection("tesha") ➞ ["esh", "sha", "tes"]
threeLetterCollection("click") ➞ ["cli", "ick", "lic"]
threeLetterCollection("cat") ➞ ["cat"]
threeLetterCollection("hi") ➞ []
threeLetterCollection("slap") ➞ ["lap", "sla"]'''

def threeshift(s):
    l=[]
    
    if len(s)<3:
        return l
    else:
        for i in range(len(s)-2):
            l+=[s[i:i+3]]
            
        k=sorted(l)
        return k
            
s=("slap")
print(threeshift(s))
