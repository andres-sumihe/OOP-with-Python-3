import math
from os import system, name
from time import sleep
from collections import defaultdict

class Account:
    '''
        MAIN CLASS
    '''
    class_list = {}
    data = []
    temp = []
    def __init__(self):
        self.class_list
        self.data
        self.temp

    def menu(self):
        print("=========================================")
        print("|       Welcome to Bank GankBank        |")
        print("=========================================")
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
        self.__ammount = float(input("Input your first deposit (min: Rp.100.000,00) : "))
        while True:
            if self.__ammount <= 0:
                print("Impossible Ammount or You are a poor one :(")
                print("input again!!!")
                self.__ammount = float(input("Input your first deposit (min: Rp.100.000,00) : "))
            elif self.__ammount < 100000:
                print("Deposited ammount must be over or equal to Rp.100.000,00")
                self.__ammount = float(input("Input your first deposit (min: Rp.100.000,00) : "))
            else: break
        self.data.append(self.__Name)
        self.data.append(self.__AccNum)
        self.data.append(self.__ammount)
        self.class_list[self.__Pin] = [self.__Name,self.__AccNum,self.__ammount]                                                    
        print("=========================================")
        print("Your Account Has Been Created")
    
    def clear(self): 
        sleep(2)
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')
        
class ATM(Account):
    def __init__(self):
        print("")
    
    def summon(self):
        self.menu()
        choice = int(input("Input Your Choice : "))
        while True:
            if choice == 1:
                self.create_account()
                break
            elif choice == 2:
                self.login()
            else:
                print("Thank You, Have A Nice Day :)")
            quit()
            self.clear()
            break
    def menuATM(self):
        print("=========================================")
        print("|                  Menu                 |")
        print("=========================================")
        print("1. Withdraw")
        print("2. Transfer")
        print("3. Check Balance")
        print("4. Next Menu")
        print("5. Log Out")
        print("6. Exit")
        print("=========================================")
        choice = int(input("Input Your Choice : "))
        while True:
            if choice == 1:
                self.withdraw()
                break
            elif choice == 2:
                self.transfer()
            elif choice == 3:
                self.display()
            elif choice == 4:
                self.display()
            elif choice == 5:
                self.summon()
            elif choice == 6:
                self.clear()
                print("You can access this apps on Github")
                print("visit github.com/andres-sumihe/OOP-with-python-3")
                print("Thanks")
                quit()

            else:
                print("Please enter valid input")
                break
        

    def login(self):
        print("=========================================")
        print("|         Sign in your account          |")
        print("=========================================")
        print(self.class_list)
        InAccNum = input("Input Your Account Number : ")
        InputPin = input("Input Your PIN :")
        for i in self.class_list:
            if InputPin == i:
                print("test", i[0])
                if self.class_list[i[0]][1] == InAccNum:
                    self.temp.append(i[0])
                    print(self.temp[0])
                    print("Login Success")
                    self.clear()
                    self.menuATM()
            else: break
        else:
            print("Your Account Not Found or Wrong Credential, Please Sign up or Try Login Again")
            self.clear()
            self.summon()
                    
    def transfer(self):
        reciever = input("Enter destination account number: ")
        amount = float(input("Enter amount to be Deposited: "))
        for i in self.class_list:
            if reciever in self.class_list[i][1]:
                self.class_list[i][2] += amount
                self.class_list[self.temp[0]][2] -= amount
                print(self.class_list[self.temp[0]][2])
                print("Found")
                break
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.class_list[self.temp[0]][2] >= amount:
            self.class_list[self.temp[0]][2] -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        self.clear()
        print("\n Net Available Balance= ", self.class_list[self.temp[0]][2])
        self.menuATM()

class online_payment(ATM):
    def __init__(self):
        print("")
    
    def menuATM(self):
        print("=========================================")
        print("|                  Menu                 |")
        print("=========================================")
        print("1. Withdraw")
        print("2. Transfer")
        print("3. Check Balance")
        print("4. Next Menu")
        print("5. Log Out")
        print("6. Exit")
        print("=========================================")
        choice = int(input("Input Your Choice : "))
        while True:
            if choice == 1:
                self.withdraw()
                self.menuATM()
            elif choice == 2:
                self.transfer()
                self.menuATM()
            elif choice == 3:
                self.display()
            elif choice == 4:
                self.summon_online_payment()
            elif choice == 5:
                self.summon()
            elif choice == 6:
                self.clear()
                print("You can access this apps on Github")
                print("visit github.com/andres-sumihe/OOP-with-python-3")
                print("Thanks")
                quit()
            else:
                print("Please enter valid input")
                break
            
    def menu_online_payment(self):
        print("=========================================")
        print("|       Welcome to Online Payment       |")
        print("=========================================")
        print("1. Pulsa")
        print("2. Token Listrik")
        print("3. About")
        print("4. Log out")
        print("5. back")
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
        print("6. Back")
        
    def token_listrik(self):
        print("\n=========================================")
        print("|    welcome to Token Listrik purchase  |")
        print("=========================================")
    
    def menu_pulsa(self):
        self.pulsa()
        choise_pulsa = int(input("Input Your Choice : "))
        while True:
            if choise_pulsa == 1:
                int(input("TELKOMSEL \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp. 5.000 \n2. Rp. 10.000 \n3. Rp. 20.000 \n4. Rp. 50.000 \n5. Rp. 100.000 \n6. Back")
                ptelkomsel = int(input("Input Your Choice: "))
                while True:
                    if ptelkomsel == 1:
                        telkomsel5 = 5000
                        if self.class_list[self.temp[0]][2] >= telkomsel5 :
                            self.class_list[self.temp[0]][2] -= telkomsel5
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 2:
                        telkomsel10 = 10000
                        if self.class_list[self.temp[0]][2] >= telkomsel10 :
                            self.class_list[self.temp[0]][2] -= telkomsel10
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 3:
                        telkomsel20 = 20000
                        if self.class_list[self.temp[0]][2] >= telkomsel20 :
                            self.class_list[self.temp[0]][2] -= telkomsel20
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 4:
                        telkomsel50 = 50000
                        if self.class_list[self.temp[0]][2] >= telkomsel50 :
                            self.class_list[self.temp[0]][2] -= telkomsel50
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 5:
                        telkomsel100 = 100000
                        if self.class_list[self.temp[0]][2] >= telkomsel100 :
                            self.class_list[self.temp[0]][2] -= telkomsel100
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("Enter the correct input")
                        self.menu_pulsa() 
                break
            elif choise_pulsa == 2:
                int(input("XL \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp. 5.000 \n2. Rp. 10.000 \n3. Rp. 20.000 \n4. Rp. 50.000 \n5. Rp. 100.000 \n6. Back")
                pxl = int(input("Input Your Choice: "))
                while True:
                    if pxl == 1:
                        pxl5 = 5000
                        if self.class_list[self.temp[0]][2] >= pxl5 :
                            self.class_list[self.temp[0]][2] -= pxl5
                            print("Xl credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 2:
                        pxl10 = 10000
                        if self.class_list[self.temp[0]][2] >= pxl10 :
                            self.class_list[self.temp[0]][2] -= pxl10
                            print("Xl credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 3:
                        pxl20 = 20000
                        if self.class_list[self.temp[0]][2] >= pxl20 :
                            self.class_list[self.temp[0]][2] -= pxl20
                            print("Xl credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 4:
                        pxl50 = 50000
                        if self.class_list[self.temp[0]][2] >= pxl50 :
                            self.class_list[self.temp[0]][2] -= pxl50
                            print("Xl credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 5:
                        pxl100 = 100000
                        if self.class_list[self.temp[0]][2] >= pxl100 :
                            self.class_list[self.temp[0]][2] -= pxl100
                            print("Xl credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("Enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 3:
                int(input("IM3 \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp. 5.000 \n2. Rp. 10.000 \n3. Rp. 20.000 \n4. Rp. 50.000 \n5. Rp. 100.000 \n6. Back")
                pim3 = int(input("Input Your Choice: "))
                while True:
                    if pim3 == 1:
                        pim35 = 5000
                        if self.class_list[self.temp[0]][2] >= pim35 :
                            self.class_list[self.temp[0]][2] -= pim35
                            print("IM3 credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 2:
                        pim310 = 10000
                        if self.class_list[self.temp[0]][2] >= pim310 :
                            self.class_list[self.temp[0]][2] -= pim310
                            print("IM3 credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 3:
                        pim320 = 20000
                        if self.class_list[self.temp[0]][2] >= pim320 :
                            self.class_list[self.temp[0]][2] -= pim320
                            print("IM3 credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 4:
                        pim350 = 50000
                        if self.class_list[self.temp[0]][2] >= pim350 :
                            self.class_list[self.temp[0]][2] -= pim350
                            print("IM3 credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 5:
                        pim3100 = 100000
                        if self.class_list[self.temp[0]][2] >= pim3100 :
                            self.class_list[self.temp[0]][2] -= pim3100
                            print("IM3 credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("Enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 4:
                int(input("AXIS \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp. 5.000 \n2. Rp. 10.000 \n3. Rp. 20.000 \n4. Rp. 50.000 \n5. Rp. 100.000 \n6. Back")
                paxis = int(input("Input Your Choice: "))
                while True:
                    if paxis == 1:
                        paxis5 = 5000
                        if self.class_list[self.temp[0]][2] >= paxis5 :
                            self.class_list[self.temp[0]][2] -= paxis5
                            print("Axis credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 2:
                        paxis10 = 10000
                        if self.class_list[self.temp[0]][2] >= paxis10 :
                            self.class_list[self.temp[0]][2] -= paxis10
                            print("Axis credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 3:
                        paxis20 = 20000
                        if self.class_list[self.temp[0]][2] >= paxis20  :
                            self.class_list[self.temp[0]][2] -= paxis20 
                            print("Axis credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 4:
                        paxis50 = 50000 
                        if self.class_list[self.temp[0]][2] >= paxis50 :
                            self.class_list[self.temp[0]][2] -= paxis50
                            print("Axis credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 5:
                        paxis100 = 100000
                        if self.class_list[self.temp[0]][2] >= paxis100 :
                            self.class_list[self.temp[0]][2] -= paxis100
                            print("Axis credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("Enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 5:
                int(input("TRI \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp. 5.000 \n2. Rp. 10.000 \n3. Rp. 20.000 \n4. Rp. 50.000 \n5. Rp. 100.000 \n6. Back")
                ptri = int(input("Input Your Choice: "))
                while True:
                    if ptri == 1:
                        ptri5 = 5000
                        if self.class_list[self.temp[0]][2] >= ptri5 :
                            self.class_list[self.temp[0]][2] -=ptri5
                            print("Tri credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 2:
                        ptri10 = 10000
                        if self.class_list[self.temp[0]][2] >= ptri10 :
                            self.class_list[self.temp[0]][2] -= ptri10
                            print("Tri credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 3:
                        ptri20 = 20000
                        if self.class_list[self.temp[0]][2] >= ptri20 :
                            self.class_list[self.temp[0]][2] -= ptri20
                            print("Tri credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 4:
                        ptri50 = 50000
                        if self.class_list[self.temp[0]][2] >= ptri50 :
                            self.class_list[self.temp[0]][2] - ptri50
                            print("Tri credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 5:
                        ptri100 = 100000
                        if self.class_list[self.temp[0]][2] >= ptri100 :
                            self.class_list[self.temp[0]][2] - ptri100
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",self.class_list[self.temp[0]][2])
                            print("\nThank You, Have A Nice Day :)")
                        else : 
                            print("The balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("Enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 6:
                online_payment()
                self.menu_online_payment()
                self.summon_online_payment()
                break
            else :
                self.menu_pulsa()
                break
            
    def menu_token_listrik(self):
        self.token_listrik()
        int(input("Enter your Token number: "))
        print("Select the credit you want to buy: ")
        print("1. Rp. 20.000 \n2. Rp. 50.000 \n3. Rp. 100.000 \n4. Rp. 150.000 \n5. Rp. 200.000 \n6. Back")
        token = int(input("Input Your Choice: "))
        while True:
            if token == 1:
                tokenlistrik20 = 20000
                if self.class_list[self.temp[0]][2] >= tokenlistrik20 :
                    self.class_list[self.temp[0]][2] -= tokenlistrik20
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", self.class_list[self.temp[0]][2])
                    print("\nThank You, Have A Nice Day :)")
                    break
                else : 
                    print("The balance is not enough!\n")
                    self.summon_online_payment()
                    break
            elif token == 2:
                tokenlistrik50 = 50000
                if self.class_list[self.temp[0]][2] >= tokenlistrik50:
                    self.class_list[self.temp[0]][2] -= tokenlistrik50
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", self.class_list[self.temp[0]][2])
                    print("\nThank You, Have A Nice Day :)")
                    break
                else : 
                    print("The balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 3:
                tokenlistrik100 = 100000
                if self.class_list[self.temp[0]][2] >= tokenlistrik100:
                    self.class_list[self.temp[0]][2] -= tokenlistrik100
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", self.class_list[self.temp[0]][2])
                    print("\nThank You, Have A Nice Day :)")
                    break
                else : 
                    print("The balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 4:
                tokenlistrik150 = 150000
                if self.class_list[self.temp[0]][2] >= tokenlistrik150:
                    self.class_list[self.temp[0]][2] -= tokenlistrik150
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", self.class_list[self.temp[0]][2])
                    print("\nThank You, Have A Nice Day :)")
                    break
                else : 
                    print("The balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 5:
                tokenlistrik200 = 200000
                if self.class_list[self.temp[0]][2] >= tokenlistrik200:
                    self.class_list[self.temp[0]][2] -= tokenlistrik200
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", self.class_list[self.temp[0]][2])
                    print("\nThank You, Have A Nice Day :)")
                    break
                else : 
                    print("The balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 6:
                    online_payment()
                    self.menu_online_payment()
                    self.summon_online_payment()
                    break
            else :
                print("Enter the correct input")
                self.menu_token_listrik()
                break


    def about(self):
        print("\n==============================================")
        print("\n|                    About                     |")
        print("\n==============================================")
        print("\n")
        print("\nVersion 1.0.1")
        print("\nAuthor : ")
        print("\n1. Andres Sumihe (672018136)")
        print("\n2. Luis Geraldo Mauboy (672018138)")
        print("\n3. Sean Alessandro Pattirane (672018112)")
        print("\n4. Ryan Renaldy Siematauw (672018096)")
        print("\n5. Farrell Giovanno Tanujaya (672018115)")
        print("\n6. Chrys Nathanael Santoso (672018135)")
        print("\n7. Adam Belo Paembonan (672018113)")
        print("\n==============================================")
        print("\n")
        print("\nVisit : Github.com/andres-sumihe/OOP-with-python-3")
        print("\n")
        print("\nJoin Our Community: ")
        print("\narisansecrity.id")
        print("\nbudakcoding.com")
        print("\ncodemaster.my.id")
        print("\n")
        print("\nContact Us: ")
        print("\n")
        print("\nadmin@codemaster.my.id")
        print("\n")
        print("\n================================================")

            
               
    def summon_online_payment(self):
        self.menu_online_payment()
        choice_online_payment = int(input("Input Your Choice : "))
        while True:
            if choice_online_payment == 1:
                self.menu_pulsa()
                break
            elif choice_online_payment == 2 :
                self.menu_token_listrik()
                break
            elif choice_online_payment == 3 :
                self.about()
                break
            elif choice_online_payment == 4 :
                self.summon()
                break
            elif choice_online_payment == 5 :
                self.menuATM()
            else:
                print("Enter the correct input")
                self.summon_online_payment()
                break

class send_money(Account):   
    def __init__(self):
        print("=========================================")
        print("|       Welcome to Send Money           |")
        print("=========================================")
    def menu_send_money(self):
        print("1. Transfers between accounts")
        print("2. Transfers Virtual Account")
        print("3. Exit")
        print("=========================================")
        
        
    def menu_tranfer_rekening(self):
        int(input("Input destination account: "))
        trans = int(input("Input Nominal to be transferred : "))
        while True:
            if self.class_list[self.temp[0]][2] >= trans :
               transfer_rek = self.class_list[self.temp[0]][2] - trans
               print("\nSuccessful! ")
               print("\nYour Balance : ",transfer_rek)
               break
            else :
                print("Your balance is not enough!!")
                break

        
    def menu_virtual_acc(self):
        int(input("Input destination Virtual Account  : "))
        trans = int(input("Input Nominal to be transferred : "))
        while True:
            if self.class_list[self.temp[0]][2] >= trans :
               transfer_rek = self.class_list[self.temp[0]][2] - trans
               print("\nSuccessful! ")
               print("\nYour Balance : ",transfer_rek)
               break
            else :
                print("Your balance is not enough!!")
                break
        
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
                print("Thank You, Have A Nice Day :)")
                break
            else:
                print("Enter the correct input")
                self.summon_send_money()
                break

s = online_payment()
while True:
    s.summon()
