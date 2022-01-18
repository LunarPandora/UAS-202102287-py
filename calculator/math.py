class Calculator:
    def __init__(self):
        self.x = int(input("\nMasukkan nilai pertama : "))
        self.y = int(input("Masukkan nilai kedua : "))
        
        self.chooseOperation()
        
    def chooseOperation(self):
        print("""
Silahkan pilih operasi yang ingin anda gunakan.      

1. Operasi penambahan (+)
2. Operasi pengurangan (-)
3. Operasi perkalian (*)
4. Operasi pembagian (/)
""")
        
        c = input("Pilih operasi perhitungan yang ingin digunakan : ")
        
        if c == "1":
            self.add()
        elif c == "2":
            self.subtract()
        elif c == "3":
            self.multiply()
        elif c == "4":
            self.divide()
        else:
            print("Pilih operasi yang telah disediakan dengan benar.")
        
    def add(self):
        return print("\nHasil pertambahan dari dua bilangan tersebut adalah " + str(self.x + self.y))
    
    def subtract(self):
        return print("\nHasil pengurangan dari dua bilangan tersebut adalah " + str(self.x - self.y))
    
    def multiply(self):
        return print("\nHasil perkalian dari dua bilangan tersebut adalah " + str(self.x * self.y))
    
    def divide(self):
        return print("\nHasil pembagian dari dua bilangan tersebut adalah " + str(self.x / self.y))