from fastapi import FastAPI
from storage import load_users
from storage import save_users
from pydantic import BaseModel
class newuser(BaseModel):
    name:str
    balance:float
    pin:str
atmapp=FastAPI()
users,nxt_acc_no=load_users("bank_data.json")
@atmapp.get("/")
def home():
    return {"message":"Welcome to ATM API!"}
@atmapp.get("/balance/{acc_no}")
def check_balance(acc_no:int):
    if acc_no not in users:
        return {"error":"User not found"}
    else:
        return {"acc_no":acc_no,"balance":users[acc_no].balance}
@atmapp.post("/deposit/{acc_no}")
def deposit(acc_no:int,amount:float):
    if acc_no not in users:
        return {"error":"User not found"}
    else:
        if amount<=0:
            return{"error":"amount must be negative"}
        else:
            users[acc_no].deposit(amount)
            return {"message":"Amount deposited successfully","Your new balance" : f"{users[acc_no].balance}"}
@atmapp.post("/withdraw/{acc_no}")
def withdraw(acc_no:int,amount:float):
    if acc_no not in users:
        return{"error":"User Not Found"}
    elif amount>users[acc_no].balance:
        return{"error":"Not enough balance"}
    else:
        users[acc_no].withdraw(amount)
        return {"message":"Amount withdrawed successfully","Your new balance" : f"{users[acc_no].balance}"}
@atmapp.get("/profile/{acc_no}")
def profile(acc_no:int):
    if acc_no not in users:
        return{"error":"User Not Found"}
    else:
        return{
            "acc_no":acc_no,
            "name":users[acc_no].name,
            "balance":users[acc_no].balance
            }
@atmapp.post("/transfer/{acc_no}/{reciever_no}")
def transfer(acc_no:int,reciever_no:int,amount:float):
    if acc_no not in users:
        return {"error":"Sender Not Found"}
    elif reciever_no not in users:
        return {"error":"Reciever not found"}
    elif amount<=0:
        return{"error":"amount must be positve"}
    elif amount>users[acc_no].balance:
        return{"error":"Not enough balance"}
    else:
        users[acc_no].send(reciever_no,amount)
        users[reciever_no].recieve(acc_no,amount)
        return {"message":f"Amount successfully sended to {reciever_no}","Your new balance" : f"{users[acc_no].balance}","reciever balance":f"{users[reciever_no].balance}rs"}
@atmapp.post("/create")
def create(user:newuser):
    global nxt_acc_no
    from atm import ATM
    users[nxt_acc_no]=ATM(nxt_acc_no,user.name,user.balance,user.pin)
    nxt_acc_no+=1
    save_users("bank_data.json",users,nxt_acc_no)
    return{"message":"Account created successfully","Your account no : ": nxt_acc_no-1}
@atmapp.post("/save")
def save():
    save_users("bank_data.json",users,nxt_acc_no)
    return {"message":"data saved successfully"}
