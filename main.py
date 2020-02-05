import math
from os import system


#Class
class Bank:
    def __init__(self):
        self.data = []
        print("===============================")
        print("Selamat Datang di Bank GankBank")
        print("===============================")

    def Create_Account(self):
        print("\n===================")
        print("Create Your Account")
        print(  "===================")
        self.name = input("Masukkan Nama Lengkap Anda : ")
        self.pin  = input("Masukkin Pin Anda : ")
        self.id   = input("Masukkin ID Anda :")
        self.data.append(self.name)

    def menu(self):
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Exit")
    

s = Bank()
s.menu()
s.Create_Account()

my_dict = {
    self.pin : [self.nama, self.ammount, self.rekening]
}


my_dict = {}

for i in my_dict:
    if pin == my_dict[i] and nama == my_dict[i][0]:
        print("login berhasil")
        a = _system('cls')
        atm()
#Inheritance


#Polymorphism


#Abstraction


#Encapsulation


#put your code here MTFK