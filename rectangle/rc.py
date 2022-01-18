def rc():
    
    p = int(input("\nMasukkan Panjang : "))
    l = int(input("Masukkan Lebar : "))
    
    luas = p * l
    keliling = 2 * (p + l)
    
    print("\nDengan panjang sebesar " + str(p) + " dan lebar sebesar " + str(l) + ", didapatkan :")
    print("Luas Persegi panjang sebesar : " + str(luas) + " SL (Satuan Luas).")
    print("Keliling Persegi panjang sebesar : " + str(keliling) + " SK (Satuan Keliling). \n")