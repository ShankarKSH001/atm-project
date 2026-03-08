from atm import ATM
import json
def load_users(filename:str)->tuple:
    try:
        users={}
        with open("bank_data.json","r")as file:
            data=json.load(file)
        nxt_acc_no=int(data["nxt_acc_no"])
        for acc_no,datas in data["users"].items():
            users[int(acc_no)]=ATM(int(datas["acc_no"]),datas["name"],float(datas["balance"]),datas["pin"])
            users[int(acc_no)].history=datas["history"]
    except(FileNotFoundError,json.JSONDecodeError, KeyError):
        nxt_acc_no=1001
    return users,nxt_acc_no
def save_users(filename:str,users:dict,nxt_acc_no:int)->None:
    data={
        "nxt_acc_no":nxt_acc_no,
            "users":{}
        }
    for acc_no,user in users.items():
        data["users"][acc_no]=user.to_dict()
    with open(filename,"w") as file:
        json.dump(data,file)
