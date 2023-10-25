from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,name,email,address,account_number,password,type):
        self.name=name
        self.email = email
        self.address = address
        self.account_number = account_number
        self.password=password
        self.balance = 0
        self.type=type
        self.transactions = []

    def deposit(self, amount,trans):
        if amount > 0:
            self.balance += amount
            self.transactions.append(trans)
            print(f'---> Amount deposited.')
        else:
            print('---> Please deposit some valid amount.')

    def withdraw(self, amount, trans):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(trans)
            print(f'--->>>>>>>>>>>>>>> Withdrawal successful.')
        else:
            print('--->>>>>>>>>>>>>>>> Withdrawal amount exceeded')


class Create_Account(Account):
    def __init__(self, name,email,address, account_number, password,type):
        super().__init__(name, email,address,account_number, password, type)
        self.loan_limit = 2
        self.loan_permission = True

    
    def check_balance(self):
        print(f'---> Your current balance is: {self.balance}')

    def transaction_history(self):
        idx = 1
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TRANSACTIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        for trans in self.transactions:
            if trans.acc_from == None:
                print(f'{idx}.Type: {trans.transaction_type} amount: {trans.amount}')
                idx+=1
            else:
                print(f'{idx} Type: {trans.transaction_type} amount: {trans.amount} from: {trans.acc_from} to: {trans.acc_to}')
                idx+=1
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TRANSACTIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    
    def take_loan(self,amount,trans):
        if self.loan_limit != 0 and self.loan_permission == True and amount > 0:
            self.transactions.append(trans)
            self.balance += amount
            self.loan_limit -= 1
            print("--->>>>>>>>>>>>>>>>>>>>>>>>>>>>> Loan transaction successful.")
        else:
            print('--->>>>>>>>>>>>>>>>>>>>>>>>>>>>> Sorry you are unable to take loan of this amount.')

    def transfer(self,amount,trans):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(trans)

super_user = Create_Account("Imtiazul Islam", "imtiajul37@gmail.com", "dhaka", "029349", "1111", "admin")
