def abstr(a,b):
    k=""
    for i in a:
        if i in b:
            continue
        else:
            k+=i
    return k

a=input()
b=input()
print(abstr(a,b))
