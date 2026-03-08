from atm import ATM
def test_deposit():
    user=ATM(1001,"Ram",5000,"1234")
    user.deposit(1000)
    assert user.balance==6000
def test_withdraw():
    user=ATM(1001,"Ram",5000,"1234")
    user.withdraw(1000)
    assert user.balance==4000
def test_negetive_balance():
    user=ATM(1001,"Ram",-5000,"1234")
    assert user.balance==0
def test_transfer():
    user=ATM(1001,"Ram",5000,"1234")
    reciever=ATM(1002,"Sam",6000,"4321")
    user.send(1002,4000)
    reciever.recieve(1001,4000)
    assert user.balance==1000
    assert reciever.balance==10000
