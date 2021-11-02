# banking system fo manager
#praveenkumar
#25-10-2021

from dbforbanking import accountdetails,balance,ATMusers,cards,pins,accnos,blockedatm,atmamount,man1,key



def addacc():
    accno=int(input("Enter A\C no:"))
    acname=input("Enter A\C holder name:").title()
    bal=int(input("Enter balance:"))
    if accno != '' and acname != '' and bal != '':
        if len(accno) > 17 or len(accno) < 17:
            accountdetails[accno] = dict(ACholdername = acname,ACnumber      = accno,branch    = "Erode",IFSC            = "SIB0756")
            balance[accno]=bal
            accnos.append(accno)
        else:
            print("Account number has been only 17 nos!!!")
            addacc()
    else:
        print("*Field Required!!!")
        addacc()


    for x,y in accountdetails[accno].items():
        print(x+":"      +y)


    ce=input("Enter 'c' to continue or b to back or 'e' to exit:")
    if ce == 'c' or ce == 'C':
        addacc()
    elif ce == 'b' or ce == 'B':
        manager()
    elif ce == 'e' or ce == 'E':
        login()

def exacc():

    for x in accountdetails:
            print(x)

    ce=input("Enter 'c' to continue or b to back or 'e' to exit:")
    if ce == 'c' or ce == 'C':
        exacc()
    elif ce == 'b' or ce == 'B':
        manager()
    elif ce == 'e' or ce == 'E':
        login()

def delacc():
    accno=input("Enter A\C no:")
    if accno != '':
        accountdetails.pop(accno)
        del accno
        for x,y in accountdetails[accno].items():
            print(x+":"      +y)
    else:
        print("*Field Required!!!")
        delacc()


    ce=input("Enter 'c' to continue or b to back or 'e' to exit:")
    if ce == 'c' or ce == 'C':
        delacc()
    elif ce == 'b' or ce == 'B':
        manager()
    elif ce == 'e' or ce == 'E':
        login()

def chebal():
    accno=int(input("Enter accno:"))
    if accno != '':
        a=balance[accno]
        print("balance"+str(a))
    else:
        print("*Field Required!!!")
        chebal()
    ce=input("Enter 'c' to continue or b to back or 'e' to exit:")
    if ce == 'c' or ce == 'C':
        delacc()
    elif ce == 'b' or ce == 'B':
        manager()
    elif ce == 'e' or ce == 'E':
        login()

def atmpro():
    accno=input("Enter A\C no:")
    if accno != '':
        x=ATMusers[accno]
        if x == "provided":
            print("Atm has been already provided successfully!!!")
        else:
            ATMusers[accno]="provided"
            print("provided succesfully")
    else:
        print("*field Required!!!")
    ce=input("Enter 'c' to continue or b to back or 'e' to exit:")
    if ce == 'c' or ce == 'C':
        delacc()
    elif ce == 'b' or ce == 'B':
        manager()
    elif ce == 'e' or ce == 'E':
        login()

def ab():
    print(x)

def atmblk():
    accno=input("Enter A\C no:")
    x=blockedatm(accno)
    print(x)
    ce=input("if you want to block or unblock(BL/UBL):").upper()
    if ce == 'BL': 
        accno=input("Enter A\C no:")
        blockedatm[accno]="blocked"
    elif ce == "UBL":
        accno=input("Enter A\C no:")
        blockedatm[accno]="unblocked"
    ce=input("Enter 'c' to continue or b to back or 'e' to exit:")
    if ce == 'c' or ce == 'C':
        delacc()
    elif ce == 'b' or ce == 'B':
        manager()
    elif ce == 'e' or ce == 'E':
        login()



def manager():
    print("Add Account(AA)\nExisting Accounts(EA)\nDelete Account(DA)\nCheck Balance(CB)\nAtm Provide(AP)\nAtm Balance(AB)\nATM bLock")
    select=input().upper()
    if select != '':
        if select == "AA":
            addacc()
        elif select == "EA":
            exacc()
        elif select == "DA":
            delacc()
        elif select == "CB":
            chrbal()
        elif select == "AP":
            atmpro()
        elif select == "AB":
            ab()
        elif select == "AL":
            atmblk()
        else:
            print("Invalid choice!!please select correct choice")
            manager()
    else:
        print("*Field Required!!")
        manager()
     
        

        
        
        


print("*******************************WELCOME TO SIB BANK****************************************************\n")
print("\t\t\t\tMANAGER PORTAL")
x=atmamount[0]

def login():
    branch=input("Enter branch name:").title()
    man=input("Enter Manager name:").title()
    pwd=input("Entr your key:")
    if branch == "Erode":
        b=man1.index(man)
        c=key.index(pwd)
        if man in man1 :
            if pwd in key and b== c:
                manager()
            else:
                print("Enter manager password correctly!!!")
                login()
        else:
            print("Enter manager name correctly!!!")
            login()
    else:
        print("Enter branch name correctly or only Erode branchers only used this!!")
login()

                
                
