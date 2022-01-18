from os import system

class Mahasiswa:
    def __init__(self):
        self.nama = input("\nMasukkan nama mahasiswa : ")
        self.alamat = input("Masukkan alamat mahasiswa : ")
        self.nim = input("Masukkan NIM : ")
        
    def showData(self):
        system('cls')
        print("\nData telah disimpan! Berikut hasil data yang terekam : \n")
        
        print("Nama mahasiswa : " + self.nama)
        print("Alamat mahasiswa : " + self.alamat)
        print("NIM : " + self.nim)