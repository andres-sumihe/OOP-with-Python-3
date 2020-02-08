import math
from os import system


#Class


class Account:
    
    def __init__(self):
        print("=========================================")
        print("|       Welcome to Bank GankBank        |")
        print("=========================================")
        self.class_list = {}
        self.data = []

    def menu(self):
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        print("=========================================")

    def create_account(self):
        print("=========================================")
        print("|        Sign up a new account         |")
        print("=========================================")
        self.__Name = input("Input your name : ")
        self.__AccNum = input("Input Your Account Number : ")
        self.__Pin  = input("Input Your PIN : ")
        self.__ammount = float(input("Input your first deposite (min: $100) : "))

        self.data.append(self.__Name)
        self.data.append(self.__AccNum)
        self.data.append(self.__ammount)
        self.class_list[self.__Pin] = self.data
        print("=========================================")
        print("Your Account Has Been Create")
        print(self.class_list)

        
    def login(self):
        print("=========================================")
        print("|         Sign in your account          |")
        print("=========================================")

        InAccNum = input("Input Your Account Number : ")
        InputPin = input("Input Your PIN :")

    def summon(self):
        s = Account()
        s.menu()
        choice = int(input("Input Your Choice : "))
        while True:
            if choice is 1:
                s.create_account()
                break
            elif choice is 2 :
                s.login()
                break
            else:
                print("Thank Your, Have A Nice Day :)")

s = Account()
while True:
    s.create_account()

class ATM(Account):
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance= ", self.balance)

# s = Account()

# while True:
#     s.menu()
#     choice = int(input("Input Your Choice : "))
#     if choice == 1 :
#         s.create_account()
#         choice3 = str(input("Press Y to go to Menu : "))
#         if choice3 == 'y' or choice3 == 'Y':
#             pass

#     elif choice == 2 :
#         s.login()
#         pass
#     elif choice == 3 :
#         print("Thank Your, Have A Nice Day :)")  
#         break


class online_payment(Account):
    def __init__(self):
        print("=========================================")
        print("|       Welcome to Online Payment       |")
        print("=========================================")
        
    def menu_online_payment(self):
        print("1. Pulsa")
        print("2. Token Listrik")
        print("3. Exit")
        print("=========================================")
        
    def pulsa(self):
        print("\n=========================================")
        print("|       welcome to pulsa purchase       |")
        print("=========================================")
        print("\nplease choose your Perdana card: ")
        print("1. TELKOMSEL")
        print("2. XL")
        print("3. IM3")
        print("4. AXIS")
        print("5. TRI")
        
    def token_listrik(self):
        print("\n=========================================")
        print("|    welcome to Token Listrik purchase  |")
        print("=========================================")
    
    def menu_pulsa(self):
        self.pulsa()
        choise_pulsa = int(input("\nInput Your Choice : "))
        while True:
            if choise_pulsa == 1:
                int(input("TELKOMSEL \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Rp.150,000 \n7. Rp.200,000")
                int(input("Input Your Choice: "))
                break
            elif choise_pulsa == 2:
                int(input("Xl \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Rp.150,000 \n7. Rp.200,000")
                int(input("Input Your Choice: "))
                break
            elif choise_pulsa == 3:
                int(input("IM3 \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Rp.150,000 \n7. Rp.200,000")
                int(input("Input Your Choice: "))
                break
            elif choise_pulsa == 4:
                int(input("AXIS \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Rp.150,000 \n7. Rp.200,000")
                int(input("Input Your Choice: "))
                break
            elif choise_pulsa == 5:
                int(input("TRI \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Rp.150,000 \n7. Rp.200,000")
                int(input("Input Your Choice: "))
                break
            else :
                self.menu_pulsa()
                break
            
    def menu_token_listrik(self):
        self.token_listrik()
        int(input("Enter your Token number: "))
        print("Select the credit you want to buy: ")
        print("1. Rp.20,000 \n2. Rp.50,000 \n3. Rp.100,000 \n4. Rp.150,000 \n5. Rp.200,000 ")
        int(input("Input Your Choice: "))
            
        
    
    def summon_online_payment(self):
        choice_online_payment = int(input("Input Your Choice : "))
        while True:
            if choice_online_payment == 1:
                self.menu_pulsa()
                break
            elif choice_online_payment == 2 :
                self.menu_token_listrik()
                break
            elif choice_online_payment == 3 :
                print("Thank Your, Have A Nice Day :)")
                break
            else:
                print("enter the correct input")
                self.summon_online_payment()
                break

# s = online_payment()  
# s.menu_online_payment()
# s.summon_online_payment()

class send_money(Account):   
    def __init__(self):
        print("=========================================")
        print("|       Welcome to Send Money           |")
        print("=========================================")
    def menu_send_money(self):
        print("1. Transfer Antar rekening")
        print("2. Transfer Virtual Account")
        print("3. Exit")
        print("=========================================")
        
        
    def menu_tranfer_rekening(self):
        int(input("Masukan rekening tujuan anda : "))
        int(input("masukan Nominal yang akan di transfer: "))
        print("\nberhasil transfer! ")
        print("\nsisa saldo anda : ")

        
    def menu_virtual_acc(self):
        int(input("Masukan No.Virtual Account yang di tuju : "))
        int(input("Masukan Nominal yang akan di transfer : "))
        print("\nberhasil transfer! ")
        print("\nsisa saldo anda : ")
        print("\ningin melakukan transaksi?")
        print("\nYa atau tidak?")
        
        
        
    def summon_send_money(self):
        choice_send_money = int(input("Input Your Choice : "))
        while True:
            if choice_send_money == 1:
                self.menu_tranfer_rekening()
                choice2 = str(input("ingin melakukan transaksi lagi? Y/N "))
                if choice2 == 'y' or choice2 == 'Y':
                    pass
                else :
                    self.menu_send_money()
                    break
            elif choice_send_money == 2 :
                self.menu_virtual_acc()
                choice3 = str(input("ingin melakukan transaksi lagi? Y/N "))
                if choice3 == 'y' or choice3 == 'Y':
                    pass
                else :
                    self.menu_send_money()
                    break
            elif choice_send_money == 3 :
                print("Thank Your, Have A Nice Day :)")
                break
            else:
                print("enter the correct input")
                self.summon_send_money()
                break

        
    
# s = send_money()
# s.menu_send_money()
# s.summon_send_money()
#Inheritance


#Polymorphism


#Abstraction


#Encapsulation


#put your code here MTFK