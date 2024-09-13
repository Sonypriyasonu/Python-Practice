'''balanced Words	
We can assign a value to each character in a word, based on their position in the alphabet (a = 1, b = 2, ... , z = 26). A balanced word is one where the sum of values on the left-hand side of the word equals the sum of values on the right-hand side. For odd length words, the middle character (balance point) is ignored.
Write a function that returns true if the word is balanced, and false if it's not.	
balanced("zips") ➞ true
// "zips" = "zi|ps" = 26+9|16+19 = 35|35 = true
balanced("brake") ➞ false
// "brake" = "br|ke" = 2+18|11+5 = 20|16 = false
Notes
All words will be lowercase, and have a minimum of 2 characters.
Palindromic words will always be balanced.'''

def balancedWords(a):
    n=len(a)
    if n>2:
        if n%2!=0:           
            l=a[:n//2]+a[n//2+1:]
        else:
            l=a
        n1=len(l)
        f=l[:n1//2]
        l=l[n1//2:]
        print(f,l)
        '''k="abcdefghijklmnopqrstuvwxyz"
        #def get_index(c):
        #    return alpha.index(c)+1
        s1=sum([k.index(c) for c in l])
        s2=sum([k.index(c) for c in f])'''
        d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        s1=0 #s1=[]
        s2=0 #s2=[]
        for i in f:
            if i in d:
                s1+=d[i] #s1+=[d[i]]
        for i in l:
            if i in d:
                s2+=d[i] #s2+=[d[i]]
        print(s1)
        print(s2)
        if s1==s2: #sum(s1)==sum(s2)
            return ("true")
        else:
            return("false")
    return "false"
                 
a=input()
print(balancedWords(a))
