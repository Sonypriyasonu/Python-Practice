def convertTime(s):
    k=s[:-2]
    p=k[2:]
    k1=int(s[:2])
    if s[-2:]=="AM":
        if k1==12:
            return ("00"+p)
        else:
            return k
    elif s[-2:]=="PM":
        if k1==12:
            return k
        else:
            return (str(k1+12)+p)
           
s=input()
print(convertTime(s))
