import sys
import pwinput
class ATM:
    def __init__(self,acc_no:int,name:str,balance:float,pin:str):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
        self.pin=pin
        self.history=[]
    @property
    def balance(self)->float:
        return self._balance
    @balance.setter
    def balance(self,value:float):
        if value<0:
            print("\nBalance cannot be negetive.\nBalance set to 0")
            self._balance=0
        else:
            self._balance=value
    def __str__(self)->str:
        return f"\nName : {self.name}\nAcc No : {self.acc_no}\nBalance : {self._balance:.2f}rs"
    def to_dict(self)->dict:
        return{
            "acc_no":self.acc_no,
            "name":self.name,
            "balance":self._balance,
            "pin":self.pin,
            "history":self.history
            }
    def deposit(self,amount:float)->None:
        while amount<=0:
            try:
                amount=float(input("\nDeposit must me possitive!\nEnter amount : "))
            except ValueError:
                amount=int(input("Enter Deposit amount in numbers : "))
        self._balance+=amount
        print(f"\nHi, {self.name} {amount}rs is credited.\nNew Balance : {self._balance}rs")
        self.history.append(("Deposit",f"{amount}rs"))
    def withdraw(self,amount:float)->None:
        while amount<=0:
            try:
                amount=float(input("\nWithdraw must me possitive!\nEnter amount : "))
            except ValueError:
                print("Enter amount in numbers!")
        while amount>self._balance:
            try:
                amount=float(input(f"\nNot Enough Balance!\nYour Balance : {self._balance}rs\nEnter amount for Withdraw :"))
            except ValueError:
                amount=int(input("Enter withdraaw amount in numbers : "))
        self._balance-=amount
        print(f"\nHi, {self.name} {amount}rs is debited.\nNew Balance : {self._balance}rs")
        self.history.append(("Withdraw",f"{amount}rs"))
    def send(self,acc_no:int,amount:float)->None:
        while amount<=0:
            try:
                amount=float(input("\nAmount must me possitive!\nEnter amount : "))
            except ValueError:
                print("Enter amount in numbers!")
        while amount>self._balance:
            try:
                amount=float(input(f"\nNot Enough Balance!\nYour Balance : {self._balance}rs\nEnter amount for Send :"))
            except ValueError:
                amount=int(input("Enter amount in numbers : "))
        self._balance-=amount
        print(f"\nHi, {self.name} {amount}rs is sended to acc no:{acc_no}.\nNew Balance : {self._balance}rs")
        self.history.append((f"sended to acc no:{acc_no} ",f"{amount}rs"))
    def recieve(self,acc_no:int,amount:float)->None:
        self._balance+=amount
        self.history.append((f"Recieved from acc no:{acc_no} ",f"{amount}rs"))
    def chk_bal(self)->None:
        print(f"\nHi, {self.name} your balance is {self._balance}rs\nTotal Transactions : {len(self.history)}")
        for transaction in self.history:
            txn_type=transaction[0]
            amount=transaction[1]
            print(f"({txn_type},{amount})")
    def veri5(self,pin:str)->None:
        attempts=1
        while pin!=self.pin:
            attempts+=1
            try:
                if attempts>3:
                    print("\nMaxiumum attempts reached! Your account is locked!")
                    sys.exit()
                pin=pwinput.pwinput(prompt=f"\nIncorrect Password\nEnter correct password {attempts}nd attempt : ",mask='*')
            except ValueError:
                print(f"\nPassword must be in numbers.")
        print("\nPassword Matched!")
