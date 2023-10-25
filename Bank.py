from Users import Create_Account
from Users import super_user
class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.__accounts = [super_user]
        self.balance = 0
        self.loan = 0
        self.__loan_feature = True
        self.__bankrupt = False
    
    def create_account(self, name,email,address,password,type):
        acc_num = len(self.__accounts) + 1
        print(len(self.__accounts))
        new_acc = Create_Account(name,email,address,acc_num,password,type)
        self.__accounts.append(new_acc)
        print(f'---> Account successfully registered.')
    # 2. Can delete any user account   
    def delete_account(self,account,t_acc_email):
        print("called")
        if account.type == 'admin':
            for acc in self.__accounts:
                if acc.email == t_acc_email:
                    self.__accounts.remove(acc)
                    print('--->>>>>>>>>>>>>>>>>>>>> Account deleted successfully')
        else:
            print('--->You are not authorized!!!')
    # 3. Can see all user accounts list 
    def see_users_account_list(self,account):
        if account.type == 'admin':
            for acc in self.__accounts:
                print(f'---> Name: {acc.name} User account type: {acc.type} User account number: {acc.account_number}')
        else:
            print('--->You are not authorized!!!')
    # 4. Can check the total available balance of the bank. 
    def check_total_available_balance(self,account):
        if account.type == 'admin':
            print(f'---> Total Available balance is: {self.balance}')
        else:
            print('---> Sorry you are not authorized!!!')
    # 5. Can check the total loan amount.
    def check_total_loan(self,account):
        if account.type == 'admin':
            print(f'---> Total Loan of {self.name} is {self.loan}tk')
        else:
            print("---> Sorry you are not authorized!!!")
    # 6. Can on or off the loan feature of the bank.   
    def change_loan_feature(self,account):
        if account.type == 'admin':
            if self.__loan_feature == True:
                self.__loan_feature = False
                print("->>>>>>>>>>>>>>>>>>>>>> Loan featured turned off")
            else:
                self.__loan_feature = True
                print("->>>>>>>>>>>>>>>>>>>>>> Loan featured turned on")
        else:
            print("---> Sorry you are not authorized!!!")
    def check_loan_feature(self):
        return self.__loan_feature
    def change_bankrupt(self,account):
        if account.type == 'admin':
            if self.__bankrupt == False:
                self.__bankrupt = True
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>This bank is bankrupt now!!!")
            else:
                self.__bankrupt = False
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>This bank is no more bankrupt!!!")
        else:
            print(">>>>>>>>>>>>>>>>>You do not have the permission to do this operation.")
    # check bankrupt
    def check_bankrupt(self):
        return self.__bankrupt
    # check valid user
    def is_valid_user(self,email):
        account = None
        for acc in self.__accounts:
            if email == acc.email:
                account = acc
                break
        return account
    
money_bank = Bank('Money Bank')
