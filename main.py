from Bank import money_bank

class Transaction_history:
    def __init__(self,desc,amount,trans_type, acc_from=None, acc_to=None) -> None:
        self.description = desc
        self.acc_from = acc_from
        self.acc_to = acc_to
        self.amount = amount
        self.transaction_type = trans_type

def main():
# Main program
    current_user=None
    while(True):
        print('--------------------WELCOME TO MONEY BANK-------------------')
        if current_user == None:
            print('---> 1. Sign in')
            print('---> 2. Sign up')
            print('---> 3. Exit')
            op = int(input("Enter: "))
            if op == 1:
                email = input("Email: ")
                isValid = money_bank.is_valid_user(email)
                if isValid == None:
                    print('---> Incorrect Email')
                    continue
                else:
                    password = input("Password: ")
                    if isValid.password != password:
                        print("---> Incorrect Password")
                        continue
                    else:
                        current_user = isValid
                        print(f'---> Successfully logged in.')
                        continue
            elif op == 2:
                print('---> 1. Savings account')
                print('---> 2. Current account')
                op = int(input('Enter: '))
                if op == 1:
                    inp_name = input('Name: ')
                    inp_email = input('Email: ')
                    isExist = money_bank.is_valid_user(inp_email)
                    if isExist == None:
                        inp_address = input('Address: ')
                        inp_password = input('Password: ')
                        inp_type = 'savings' 
                        money_bank.create_account(inp_name,inp_email,inp_address,inp_password,inp_type)
                        continue
                    else:
                        print("------------->>>>>>>>>>> User already exist.")
                        continue
                elif op == 2:
                    inp_name = input('Name: ')
                    inp_email = input('Email: ')
                    isExist = money_bank.is_valid_user(inp_email)
                    if isExist == None:
                        inp_address = input('Address: ')
                        inp_password = input('Password: ')
                        inp_type = 'current' 
                        money_bank.create_account(inp_name,inp_email,inp_address,inp_password,inp_type)
                        continue
                    else:
                        print("------------->>>>>>>>>>> User already exist.")
                        continue
                else:
                    print("------------->>>>>>>>>>> Please enter a valid input.")
                    continue
            elif op == 3:
                break
            else:
                print("Please enter a valid input.")
                continue
        # user already logged in
        else:
            #check if user admin
            if current_user.type == 'admin':
                #show admin functionality
                print('---->>>>>>>>>>>>>>>>>>>>>>>>>>> ADMIN<<<<<<<<<<<<<<<<<<<<<<<<<<<-------')
                print("--->> 1. Create an account")     
                print("--->> 2. Delete an account")     
                print("--->> 3. See all users account")     
                print("--->> 4. Check total balance of the bank")     
                print("--->> 5. Check total loan amount")     
                print("--->> 6. Turn on/off loan feature")     
                print("--->> 7. Turn on/off bankrupt status")     
                print("--->> 8. Log-out") 
                print('--->> 9. Exit')
                option = int(input("Enter option: "))  
                # create an admin account
                if option == 1:
                    inp_name = input('Name: ')
                    inp_email = input('Email: ')
                    isExist = money_bank.is_valid_user(inp_email)
                    if isExist == None:
                        inp_address = input('Address: ')
                        inp_password = input('Password: ')
                        inp_type = 'admin' 
                        money_bank.create_account(inp_name,inp_email,inp_address,inp_password,inp_type)
                        continue
                    else:
                        print("------------->>>>>>>>>>> User already exist.")
                        continue 
                # Delete user
                elif option==2:
                    del_email = input('Enter deletable acount email: ')
                    user = money_bank.is_valid_user(del_email)
                    if user == None:
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>User does not exists')
                        continue
                    elif user.email == 'imtiajul37@gmail.com':
                        print("Sorry super user can not be deleted!!!")
                        continue
                    elif user.email == current_user.email:
                        permission = input("Are you sure you want to delete your account? (yes/no)")
                        if permission == 'yes':
                            money_bank.delete_account(current_user,del_email)
                            continue
                        elif permission == 'no':
                            continue
                        else:
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Incorrect input!!!")
                            continue
                    else:
                        money_bank.delete_account(current_user,del_email)
                        continue
                elif option==3:
                    money_bank.see_users_account_list(current_user)
                    continue
                elif option == 4:
                    money_bank.check_total_available_balance(current_user)
                    continue
                elif option == 5:
                    money_bank.check_total_loan(current_user)
                    continue
                elif option == 6:
                    money_bank.change_loan_feature(current_user)
                    continue
                elif option == 7:
                    money_bank.change_bankrupt(current_user)
                    continue
                elif option == 8:
                    current_user = None
                    continue
                elif option == 9:
                    break
                else:
                    print("Not valid option")
                    continue
            
            
            else:
                #show user functionality  
                print(f'>>>>>>>>>>>>>>>>>>>>>WELCOME {current_user.name}<<<<<<<<<<<<<<<<<<<<<<<<')
                print("--->> 1. Deposit")     
                print("--->> 2. Withdraw")     
                print("--->> 3. Check balance")     
                print("--->> 4. Check transaction history")     
                print("--->> 5. Take loan")     
                print("--->> 6. Transfer") 
                print("--->> 7. Logout") 
                print('--->> 8. Exit')
                option = int(input("Enter option: ")) 
                # User can register an account
                
                # User can deposit
                if option == 1:
                    amount = int(input('Enter amount: '))
                    if amount > 0:
                        money_bank.balance += amount
                    trans = Transaction_history("Depositing money",amount,'deposit')
                    current_user.deposit(amount,trans)
                    continue
                # Withdraw
                elif option == 2:
                    if money_bank.check_bankrupt() == True:
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>The bank is bankrupt")
                    else:
                        amount = int(input('Enter amount: '))
                        money_bank.balance -= amount
                        trans = Transaction_history("Withdrawal", amount,'withdraw')
                        current_user.withdraw(amount,trans)
                        continue
                # Balance check
                elif option == 3:
                    current_user.check_balance()
                    continue
                # Check account history
                elif option == 4:
                    current_user.transaction_history()
                    continue
                # Can take a loan from the bank at most two times.
                elif option == 5:
                    if money_bank.check_loan_feature() == True and money_bank.check_bankrupt() == False:
                        amount = int(input('Enter amount: '))
                        trans = Transaction_history("Taking loan from bank", amount, 'loan')
                        current_user.take_loan(amount, trans)
                        money_bank.balance -= amount
                        money_bank.loan += amount
                        continue
                    else:
                        print('>>>>>>>>>>>>>>>>>>>>>> Sorry loan service is currently unavailable.')
                        continue
                # Can transfer the amount from his account to another user account. if the other account does not exist then show an error message “Account does not exist”. 
                elif option == 6:
                    acc_email = input('Account email: ')
                    if acc_email == current_user.email:
                        print("You can not transfer money to yourself")
                    else:
                        to_user = money_bank.is_valid_user(acc_email)
                        if to_user == None:
                            print('-->>>>>>>>>>>>>>>>>>>>>>>>>>> User does not exist')
                            continue
                        else:
                            trans_amount = int(input("Enter amount: "))
                            if trans_amount > current_user.balance:
                                print('--->>>>>>>>>>>>>>>>>>>>>>> Insufficient balance')
                                continue
                            else:
                                from_acc_trans = Transaction_history(f'Transfer amount to: {acc_email}',trans_amount,'transfer','self', to_user.email)
                                to_acc_trans = Transaction_history(f'Transfer amount from: {current_user.email}', trans_amount, 'transfer',current_user.email, 'self')
                                current_user.balance -= trans_amount
                                to_user.balance += trans_amount
                                current_user.transactions.append(from_acc_trans)
                                to_user.transactions.append(to_acc_trans)
                                print('--->>>>>>>>>>>>>>>>>>>>>>>>Transfer successful.')
                                continue
                elif option == 7:
                    current_user = None
                    continue
                elif option == 8:
                    break
                else:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>Please enter a valid option")
                    continue
                
if __name__ == '__main__':
    main()
