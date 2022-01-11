class Bank_Account:
    def __init__(self,name,account_num):
        self.name=name
        self.account_num=account_num
        self.balance=0
        self.overdraft_limit=-2000
        self.transaction=[]
    def statment(self):
        print(f"name:{self.name} balance:{self.balance} account number:{self.account_num}\n transaction:{self.transaction}")
    def withdarw(self,amount):
        if self.balance-amount>=self.overdraft_limit:
            self.balance-=amount
            self.transaction.append(-amount)
        else:
            print("you dont have money to withdraw")
        
    def deposit(self,amount):
        self.balance+=amount
        self.transaction.append(amount)
    def is_overdraft(self):
        if self.balance<0:
            return True
        else:
            return False

my_account=Bank_Account("ben",496587)
my_account.statment()
my_account.deposit(2000)
my_account.statment()
my_account.withdarw(5000)