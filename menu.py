from os import system
from rectangle.rc import rc
from input_data_with_class import mahasiswa
from calculator import math

repeat = True

def clearWindow():
    system('cls')

while repeat :
    print("""
    Selamat datang!
    Silahkan pilih program yang ingin anda jalankan.      

    1. Menghitung luas persegi panjang
    2. Menginput data mahasiswa
    3. Kalkulator sederhana
    """)

    pilihan = input("Pilihan : ")
    
    if pilihan == "1":
        rc()
    elif pilihan == "2":
        a = mahasiswa.Mahasiswa()
        a.showData()
    elif pilihan == "3":
        a = math.Calculator()
    
    replay_program = input('Apakah anda ingin mengulang program? (y/n):').lower()
      
    if replay_program == 'y':
        clearWindow()
    elif replay_program == 'n':
        repeat = False
        raise SystemExit()
    else:
        raise SystemExit()

