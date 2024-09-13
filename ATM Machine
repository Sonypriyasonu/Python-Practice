'''
Write a program for a simplified ATM (Automated Teller Machine) that performs two basic operations: 
deposit and withdraw. The ATM should handle transactions in denominations of 100, 200, 500, and 2000 
rupee notes. Implement a simple menu-driven program where the user can choose to deposit or 
withdraw money. Ensure that the program updates the available cash in the ATM accordingly. 
 
The program should initialize the ATM with some initial amount of cash.
Implement functions/methods for deposit and withdraw operations.
Display the available cash in the ATM after each transaction.
The program should continue running until the user chooses to exit

Deposit: Customer inputs the number of currency notes in each denomination
D.1) If any input values are negative, print "Incorrect deposit amount".
D.2) If all the input values are zero, print "Deposit amount cannot be zero".
D.3) If the input values are valid, increment the balances of corresponding rupee notes and print 
the available new balances in each denomination and the total balance.

Withdraw: Customer input the amount to withdraw. ATM dispenses the 2000, 500, 200, and 100 rupee
notes needed.

W.1) If the input amount is zero, negative, or over the current balance, print "Incorrect or 
insufficient funds".
W.2) If the input amount is in valid range, print the number of currency notes dispensed in each 
denomination. Use the available higher denomination first. Also, print the available new 
balances in each denomination and the total balance.'''

global n,d
n=280000
d={2000:100,500:100,200:100,100:100}
def deposit():
    global n,d
    k={2000:int(input("Enter no. of 2000 notes ")),
        500:int(input("Enter no. of 500 notes ")),
        200:int(input("Enter no. of 200 notes ")),
        100:int(input("Enter no. of 100 notes "))}
    c=0
    for i in k:
        c+=k[i]
    if c<0:
        print("\nIncorrect deposit amount")
    elif c==0:
        print("\nDeposit amount cannot be zero")
    elif c>0:
        for i in d:
            d[i]=d[i]+k[i]  
        print("Total available balance: ",atmbal())
        print("Notes available in ATM: ", d)
    
    
def atmbal(): 
    global d,n
    n = sum(key*value for key,value in d.items())
    return n
    #print("Total available balance ",n)


def check_den(cash):
    global n,d
    res=cash
    withdrawn_notes={}
    for i in d:   #2000,500,100,200
        if d[i]<=0:
            continue
        
        notes=min(res//i,d[i])
        if notes>0:
            withdrawn_notes[i]=notes
            res-=notes*i
            
        if res==0:
            break
    if res==0:
        for key,value in withdrawn_notes.items():
            d[key]-=value
            n-=key*value
        print("\nAmount withdrawn Successfully!")
        print("\nNotes withdrawn:", withdrawn_notes)
        return True
    else:
        print("\nIncorrect or Insufficient funds ")
        return True
        
def withdraw():
        withdr_amt=int(input("Enter Amount "))
        if withdr_amt<=0:
            print("Incorrect or Insufficient funds ")
        else:
            check_den(withdr_amt)
            print("Available Balance: ",n)

    
def AtmMachine():
    while True:
        print("\nEnter '1' to deposit ")
        print("Enter '2' to withdraw ")
        print("Enter '3' to check balance")
        print("Enter '4' to exit ")
        ask=int(input())
        if ask==1:
            deposit()        
        elif ask==2:
            withdraw()
        elif ask==3:
            print("Available Balance",n)
        elif ask==4:
            print("Transaction completed")
            break
        else:
            print("Incorrect input")
        
AtmMachine()
