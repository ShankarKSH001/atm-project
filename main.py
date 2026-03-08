from atm import ATM
from storage import load_users,save_users
import pwinput
users,nxt_acc_no=load_users("bank_data.json")
acc_no=None
while True:
    try:
        menu=int(input("\n1 for create users\n2 for login\n3 for Deposit\n4 for Withdraw\n5 for Transfer money\n6 for Check Balance\n7 for logout\n8 for exit\n9 for print your profile\n\nChoose your method : "))
    except ValueError:
        print("\nEnter in numbers!")
    if menu==1:
        try:
            name=input("\nEnter name : ")
            balance=float(input(f"Hi, {name} Enter your initial balance : "))
            pin=pwinput.pwinput(prompt="Set your pin : ",mask='*')
            users[nxt_acc_no]=ATM(nxt_acc_no,name,balance,pin)
            print(f"Hi, {name} Account created successfully!\nYour Acc number = {nxt_acc_no}")
            nxt_acc_no+=1
        except ValueError:
            print("\nEnter  in numbers!")
    elif menu==2:
        if acc_no is None:
            if len(users)<=0:
                print("\nCreate users first")
                continue
        else:
            print("\nLogout First.")
            continue
        try:
            acc_no=int(input("\nEnter your Account no : "))
            while acc_no not in users:
                acc_no=int(input("\nUser Not Found\nEnter your Account no : "))
            pin=pwinput.pwinput(prompt="Enter your password : ")
            users[acc_no].veri5(pin)
        except ValueError:
            print("\nEnter in numbers!")
    elif menu==3:
        try:
            pin=pwinput.pwinput(prompt="Enter your password : ")
            users[acc_no].veri5(pin)
            amount=float(input("\nEnter amount to Deposit : "))
            users[acc_no].deposit(amount)
        except ValueError:
            print("\nAmount must be in numbers")
    elif menu==4:
        try:
            pin=pwinput.pwinput(prompt="Enter your password : ")
            users[acc_no].veri5(pin)
            amount=float(input("\nEnter amount to Withdraw : "))
            users[acc_no].withdraw(amount)
        except:
            print("\nAmount must be in numbers")
    elif menu==5:
        try:
            pin=pwinput.pwinput(prompt="Enter your password : ")
            users[acc_no].veri5(pin)
            reciever_no=int(input("\nEnter Reciever account no : "))
            while reciever_no==acc_no:
                reciever_no=int(input("\nYou can't send yourself\nEnter Reciever account no correctly : "))
            while reciever_no not in users:
                reciever_no=int(input("\nEnter Reciever account no correctly : "))
            amount=float(input("\nEnter amount to send : "))
            users[acc_no].send(reciever_no,amount)
            users[reciever_no].recieve(acc_no,amount)
        except ValueError:
            print("\nEnter in numbers!")
    elif menu==6:
        users[acc_no].chk_bal()
    elif menu==7:
        print("You logged out successfully.")
        acc_no = None
    elif menu==8:
        save_users("bank_data.json",users,nxt_acc_no)
        print("\ndata saved successfully!")
        print("\nThanks for using our ATM!")
        break
    elif menu==9:
            if acc_no is None:
                print("\nLogin First")
                continue
            print(users[acc_no])
