'''
5Q)
 
Write a function that selects all words that have all the same vowels (in any order and/or number) 
as the first word, including the first word.
Examples

sameVowelGroup(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]
sameVowelGroup(["many", "carriage", "emit", "apricot", "animal"]) 
                 ➞ ["many", "carriage", "apricot", "animal"]
sameVowelGroup(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
 
Notes
Words will contain only lowercase letters, and may contain whitespaces.
Frequency does not matter (e.g. if the first word is "loopy", then you can include words with any 
number of o's, so long as they only contain o's, and not any other vowels).'''

def findvowel(l):
    k=""
    for j in l[0]:
        if j in "aeiou":
            k+=j               
    return k

def samevowel(l):
    k=findvowel(l)
    m=[]
    for i in l:
        for j in i:
            if j in k:
                m.append(i)
                break
            '''if i not in m:
                   m.append(i)
                   break'''
    return m

l=["hoops", "chuff", "bot", "bottom"]
print(samevowel(l))
