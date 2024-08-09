class ATMCard:
    def __init__(self, card_number, expiration_date, cvv, account_number, cardholder_name):
        
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cardholder_name = cardholder_name
        
        
        self.__cvv = cvv
        self.__account_number = account_number

    
    def get_card_number(self):
        return self.card_number

    
    def get_expiration_date(self):
        return self.expiration_date

    
    def get_cardholder_name(self):
        return self.cardholder_name

   
    def display_account_info(self):
        return f"Account Holder: {self.cardholder_name}\nCard Number: {self.card_number}\nExpiry Date: {self.expiration_date}"

    
    def validate_cvv(self, input_cvv):
        return input_cvv == self.__cvv


my_card = ATMCard(
    card_number="1234 5678 9012 3456",
    expiration_date="12/25",
    cvv="678",
    account_number="9876543210",
    cardholder_name="Yash Shrivastav"
)



print("Welcome to SBI bank ATM!")
print("Please Insert your Card:")

pin=1234
chances= 3
balance= 5000

        
while chances!=0:
    user_pin=int(input("Enter your 4 digit ATM PIN:"))
    if(user_pin!=pin):
        chances-=1
        print("Sorry! you have entered wrong PIN")
        print(f"You have{chances} chances left")
    else:
        choice_type=input("Type of card you have:\n1 = Debit\n2 = Credit\n")
    
        if(choice_type=="1"):
            user_choice= input("1 : Balance \n2 : Withdrawal \n3 : Deposit\n4 : Update PIN\n5 : Display_account_info\n")
        

            if (user_choice =="1"):
                print("Your current balance is Rs.",balance)
                print("===================================================================")

            elif(user_choice=="2"):
                deposited_amount=int(input("Enter the amount you want to deposit:"))
                total_balance=(balance+deposited_amount)
                print("Rs.",deposited_amount,"is credited in your account")
                print("Your current balance is Rs.",total_balance)
                print("===================================================================")

            elif(user_choice == "3"):
                withdraw_amount=int(input("Enter the amount you want to withdraw:"))
                if(withdraw_amount<=balance):
                    total_balance=(balance-withdraw_amount)
                    print("Rs.",withdraw_amount,"is debited from your account:")
                    print("Your current balance is Rs.",total_balance)
                    print("===================================================================")
                else:
                    print("You donot have sufficient balance")
                    print("===================================================================")


            elif(user_choice == "4"):
                current_pin=int(input("Enter current PIN ~"))
                if(current_pin == pin):
                    new_pin=int(input("Enter new PIN ~"))
                    confirm_new_pin=int(input("Confirm new PIN ~"))
                    if(new_pin == confirm_new_pin):
                        print("PIN updated successfully!")
                    else:
                        print("New PIN and confirmation new PIN donot match.")
                else:
                    print("You  have entered wrong PIN")
            elif(user_choice == "5"):
                print(my_card.display_account_info())



                
        elif(choice_type=="2"):
            user_choice= input("1 : Balance \n2 : Withdrawal \n3 : Update PIN\n4 : Display account info\n")

            if (user_choice =="1"):
                print("Your current balance is Rs.",balance)
                print("===================================================================")
                
            elif(user_choice == "2"):
                withdraw_amount=int(input("Enter the amount you want to withdraw:"))
                if(withdraw_amount<=balance):
                    total_balance=(balance-withdraw_amount)
                    print("Rs.",withdraw_amount,"is debited from your account:")
                    print("Your current balance is Rs.",total_balance)
                    print("===================================================================")
                else:
                    print("You donot have sufficient balance")
                    print("===================================================================")

            elif(user_choice == "3"):
                current_pin=int(input("Enter current PIN ~"))
                if(current_pin == pin):
                    new_pin=int(input("Enter new PIN ~"))
                    confirm_new_pin=int(input("Confirm new PIN ~"))
                    if(new_pin == confirm_new_pin):
                        print("PIN updated successfully!")
                    else:
                        print("New PIN and confirmation new PIN donot match.")
                else:
                    print("You  have entered wrong PIN")

            elif(user_choice == "4"):
                print(my_card.display_account_info())



    user_exit=input("would you like to exit? yes/no:\n")
    if(user_exit=="yes"):
        print("Thankyou for using SBI ATM!!\nHave a nice day!")
        break
    else:
        continue








