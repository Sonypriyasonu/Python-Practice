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

'''24-Hour Time	
Write a function that receives the time in 12-hour AM/PM format and 
returns a string representation of the time in railway (24-hour) format.	
convertTime(“07:05:45PM”) ➞ “19:05:45”
convertTime(“12:40:22AM”) ➞ “00:40:22”
convertTime(“12:45:54PM”) ➞ “12:45:54”'''
