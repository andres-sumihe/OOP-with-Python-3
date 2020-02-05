import math
from os import system


#Class


class Account:
    class_list = {}
    int
    a = 1
    int
    b = 2
    int
    c = 3
    def __init__(self):
        print("=========================================")
        print("|       Welcome to Bank GankBank        |")
        print("=========================================")

    def menu(self):
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        print("=========================================")

    def create_account(self):
        print("=========================================")
        print("|        Sign up an new account         |")
        print("=========================================")
        self.__Name = input("Input your name : ")
        self.__AccNum = input("Input Your Account Number : ")
        self.__Pin  = input("Input Your PIN : ")
        self.__ammount = float(input("Input your first deposite (min: $100) : "))


        Account.class_list[Account.a] = self.__AccNum  # Pake ini ga bisa simpan value lebih dari satu
        Account.class_list[Account.b] = self.__Pin     # artinya gak bisa bikin 2 akun
        Account.class_list[Account.c] = self.__ammount # gmna dong ? :(
        print("=========================================")
        print("Your Account Has Been Create")
        print(Account.class_list[Account.a])
        for i in Account.class_list[Account.a]:
            print(i)
        
    def login(self):
        print("=========================================")
        print("|         Sign in your account          |")
        print("=========================================")

        InAccNum = input("Input Your Account Number : ")
        InputPin = input("Input Your PIN :")
        for i in Account.class_list[Account.b]:
            print(i)  #gw cuma test valuenya apa,
            # if InputPin == Account.class_list[Account.b][i] and InAccNum == Account.class_list[Account.a][i]:
            #     print("Success")
            # else:
            #     print("Failed")

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



class ATM(Account):
    def __init__(self, withdraw):
        self.withdraw = 0

    def makeWithdraw(self):
        withdraw = float(input("Input Ammount for withdraw: "))
        Account.class_list[Account.c]-= withdraw
        print("You withdraw: " + str(withdraw)+ "Success")




s = Account()

while True:
    s.menu()
    choice = int(input("Input Your Choice : "))
    if choice == 1 :
        s.create_account()
        choice3 = str(input("Press Y to go to Menu : "))
        if choice3 == 'y' or choice3 == 'Y':
            pass

    elif choice == 2 :
        s.login()
        pass
    elif choice == 3 :
        print("Thank Your, Have A Nice Day :)")  
        break





#Inheritance


#Polymorphism


#Abstraction


#Encapsulation


#put your code here MTFK