import math

def Menu():
    print("-------------------------Menu-------------------------")
    print("1. Registrasi")
    print("2. Daftar Menu")
    print("3. Cari Menu")
    print("4. Clear Menu")
    print("5. Delete Menu")
    print("6. Exit")
    print("\n")

def Registrasi(myList):
    jumlah = int(input("Masukan Jumlah Makanan yang mau didaftarkan : "))
    for i in range(jumlah):
        makanan = input("Masukan Menu Makanan : ")
        myList.append(makanan)
        print("Makanan Berhasil dimasukan\n")

def Daftar(myList):
    no = 1
    print("Daftar Menu")
    if len(myList) < 1:
        print("Anda Tidak Memiliki Daftar Menu")
    for i in myList:
        print(str(no)+". "+i)
        no +=1
    print("\n")

def Cari(myList):
    cari = input("Masukan menu yang akan dicari : ")
    if cari in myList:
        print("Menu "+cari+" ada di dalam daftar menu")
    else:
        print("Maaf menu yang anda cari tidak ada di dalam daftar menu")

def ClearMenu(myList):
    if len(myList) < 1:
        print("Anda Tidak Memiliki Daftar Menu")
        pass
    else:
        jumlahList = len(myList)
        konfirmasi = input("Apakah anda yakin akan menghapus semua daftar menu ? (Y/N) : ")
        if konfirmasi == "Y" or konfirmasi == "y":
            myList.clear()
            print(str(jumlahList)+ " menu telah dihapus")
        elif konfirmasi == "n" or konfirmasi == "n":
            pass
        else: print("Maaf, masukan Y/N")

def DeleteMenu(myList):
    print("Daftar Menu")
    no = 1
    for i in myList:
        print(str(no)+". "+i)
        no +=1
    hapus = input("Masukan menu yang akan di hapus : ")
    if hapus in myList:
        myList.remove(hapus)
    else:
        print("Maaf menu yang anda masukan tidak ada di dalam daftar\n")


#Main Program
myList = []
while True:
    Menu()
    pilihan = int(input("Masukan Pilihan Menu : "))

    if pilihan == 1:
        Registrasi(myList)
    elif pilihan == 2:
        Daftar(myList)
    elif pilihan == 3:
        Cari(myList)
    elif pilihan == 4:
        ClearMenu(myList)
    elif pilihan == 5:
        DeleteMenu(myList)
    elif pilihan == 6:
        print("Terima kasih")
        quit()
    else: print("Pilihan anda salah, harap masukan hanya angka")

