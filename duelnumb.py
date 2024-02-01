#menampilkan angka acak
from random import randint
numRan = randint(0,20)

numIn = int(input("Pilih satu angka antara 1-20 : "))
if(numIn > 20):
    print("Input tidak sesuai!")
else:
    print("Player\t\t:", numIn)
    print("Computer\t:", numRan)
    if(numIn > numRan):
        print("Kamu menang!")
    elif (numIn == numRan):
        print("Seri")
    else:
        print("Kamu kalah!")
