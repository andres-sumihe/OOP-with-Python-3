import math
from os import system


#Class

def cls():
    os.system("cls")

class Account:
    class_list = {}
    int
    a = 1
    int
    b = 2
    int
    c = 3
    clear = lambda: os.system('cls')
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
        self.Name = input("Input your name : ")
        self.AccNum = input("Input Your Account Number : ")
        self.Pin  = input("Input Your PIN : ")


        Account.class_list[Account.a] = self.AccNum
        Account.class_list[Account.b] = self.Pin
        print("=========================================")
        print("Your Account Has Been Create")
        
    def login(self):
        print("=========================================")
        print("|         Sign in your account          |")
        print("=========================================")

        InAccNum = input("Input Your Account Number : ")
        InputPin = input("Input Your PIN :")

        if InputPin == Account.class_list[Account.b] and InAccNum == Account.class_list[Account.a]:
            print("Success")
        else:
            print("Failed")

    def summon(self):
        s = Account()
        s.menu()
        choice = int(input("Input Your Choice : "))
        if choice is 1:
            s.create_account()
        elif choice is 2 :
            s.login()
        else:
            print("Thank Your, Have A Nice Day :)")


s = Account()
s.menu()
choice = int(input("Input Your Choice : "))
if choice is 1 :
    s.create_account()
    choice3 = str(input("Press Y to go to Menu : "))
    if choice3 is 'y' or choice3 is 'Y':
        s.summon()

elif choice is 2 :
    print("Please Create Your Account Before Sign Up")
    choice2 = str(input("Press Y to Sign Up : "))
    if choice2 is 'y' or choice2 is 'Y':
        s.create_account()
        s.summon()
elif choice is 3 :
    print("Thank Your, Have A Nice Day :)")





#Inheritance


#Polymorphism


#Abstraction


#Encapsulation


#put your code here MTFK