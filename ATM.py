'''
Make a program for ATM
enter 4 digit code ( if wrong for 4 times exit)
show withdrawal, check balance, deposit, return card in screen
If the person has 300 in account, show him balance at the end for withdrawal, check balance, deposit
Add program here, if the person doesn't complete in 5 s timeout
'''
from time import *
import threading, queue, os
queue = queue.Queue()
global timer

def mainprogram():

    amount = 300.0
    r = int(input("Enter 1 for Withdrawal\n\t  2 for deposit\n\t  3 for balance\n"))
    queue.put(r)
    if (r==1):
        wa=float(input("Enter withdrawal amount\n"))
        amount=amount-wa
        if amount<0:
            print("Withdrawal is more than account")
        else:
            print ("Withdrawal complete, The new balance is", amount)
    elif (r==2):
        de=float(input("Enter deposit amount\n"))
        amount=amount+de
        print ("Deposit complete, The new balance is", amount)
    elif (r==3):
        print ("The balance is", amount)


# Timer Program
print("Welcome to the ATM\n")
c=0
while(c<4):
    a=int(input(" Enter the 4 digit code\n"))
    if(a!=2345):
        print("Wrong pin, try again")
        c=c+1
        if (c>3):
            print("Get out")
            os._exit(0)
    else:
        c=5

countdown_thread=threading.Thread(target=mainprogram)
countdown_thread.start()
timer = 5
for x in range(timer):
    timer = timer - 1
    sleep(1)
if (queue.empty()==True):
    print("\n\n Time out")
    os._exit(0)