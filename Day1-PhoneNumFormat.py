'''
Phone Number Formatting	
Create a method that takes an array of 10 integers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).
formatPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) ➞ "(123) 456-7890"
formatPhoneNumber([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]) ➞ "(519) 555-4468"
formatPhoneNumber([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]) ➞ "(345) 501-2527"
'''

def formatPhoneNumber(k):
    s=""
    for i in range(0,10):
        p="("
        q=")"
        r="-"
        if i==0:
            s+=p+str(k[i])
        elif i==2:
            s+=str(k[i])+q+" "
        elif i==5:
            s+=str(k[i])+r
        else:
            s+=str(k[i])
    return s

k=list(map(int,input().split()))
print(formatPhoneNumber(k))
