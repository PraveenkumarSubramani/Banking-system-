from dbforbanking import accountdetails,balance,ATMusers,cards,pins,accnos,blockedatm,atmamount


def atm():
    amt=int(input("Enter amount:"))
    if amt > x:
        if amt > balance[accno]:
            print("Insufficient balance!!!")
            ce=input("Enter 'c' to continue or 'e' to exit:")
            if ce == 'c' or ce == 'C':
                atm()
            elif ce == 'e' or ce == 'E':
                main()
        else:
            print("Collect your cash!!!")
            ab=balance[accno]-amt
            balance[accno]=ab
            atmamount=x-amt
            print("Available balance:"+str(ab))
            ce=input("Enter 'c' to continue or 'e' to exit:")
            if ce == 'c' or ce == 'C':
                atm()
            elif ce == 'e' or ce == 'E':
                print("THANK YOU VISIT AGAIN!!!!")
    else:
        print("SORRY WE CAN'T PROVIDE THIS TRANSACTION!!!")
        ce=input("Enter 'c' to continue or 'e' to exit:")
        if ce == 'c' or ce == 'C':
            atm()
        elif ce == 'e' or ce == 'E':
            print("THANK YOU VISIT AGAIN!!!!")

def balancecheck():
    x=balance[accno]
    print(x)
    ce=input("Enter 'c' to continue or 'e' to exit:")
    if ce == 'c' or ce == 'C':
        main()
    elif ce == 'e' or ce == 'E':
        print("THANK YOU VISIT AGAIN!!!!")
    
    
def main():

    for x,y in accountdetails[accno].items():
        print(x+"     "+y)


    bcow=input("withdraw(W)\nbalance check(BC):").upper()
    if bcow == "W":
        atm()
    elif bcow == "BC":
        balancecheck()
            



print("*****************Welcome to SIB ATM********************")
x=atmamount[0]
for i in range(3):
    cardno = int(input("Enter your card number:"))
    pin=int(input("Enter your pin number:"))
    accno=int(input("accno:"))
    if cardno in cards:
        if pin in pins:
            if accno in accnos:
                x=cards.index(cardno)
                y=pins.index(pin)
                a=accnos.index(accno)
                if x == y and x == a:
                    if blockedatm[accno] != "blocked":
                         main()
                    else:
                        print("YOUR CARD HAS BEEN BLOCKED,CONTACK YOUR BRANCH!!!")
            else:
                print("WE CANNOT FETCH YOUR ACCOUNT,ENTER VALID ACC NO ")
        else:
            print("WE CANNOT FETCH YOUR ACCOUNT,ENTER VALID ATM PIN ")
    else:
        print("WE CANNOT FETCH YOUR ACCOUNT,ENTER VALID CARD NO")
print("YOUR CARD HAS BEEN BLOCKED DUE TO TOO MANY WTONG ATTEMPTS,CONTACT YOUR BRANCH!!!")
blockedatm[accno]="blocked"   


                    
        
        


        
