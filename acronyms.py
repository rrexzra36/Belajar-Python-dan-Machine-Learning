user_name = str(input("Masukkan nama anda\t: "))
user_nim = str(input("Masukkan nim anda\t: "))

nama = user_name.split()
# nim = user_nim.count()
a = ""

for i in nama:
    a = a + str(i[0]).upper()
    if(len(a) == len(nama)):
        print("Kode anda\t: ", a + user_nim[6:])