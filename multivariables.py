import time
import datetime

yearnow = datetime.datetime.now()
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

name = str(input("Nama\t: "))
date = int(input("Tanggal\t: "))
month = int(input("Bulan (angka) \t: "))
year = int(input("Tahun\t: "))

print("=============================")
print("Nama\t:", name)
print("Tanggal\t:", date, months[month-1], year)
print("Umur\t:", yearnow.year - year)