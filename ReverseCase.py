'''
Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
Examples
 
reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"
reverseCase("MANY THANKS") ➞ "many thanks"
reverseCase("sPoNtAnEoUs") ➞ "SpOnTaNeOuS"'''

def reverseStr(s):
    a="qwertyuiopasdfghjklzxcvbnm"
    b="QWERTYUIOPASDFGHJKLZXCVBNM"
    k=""
    for i in s:
        if i in a:
            k+=i.upper()
        elif i==" ":
            k+=" "
        elif i in b:
            k+=i.lower()
    return k
s="hAPPY bIRTHDAY"
print(reverseStr(s))
