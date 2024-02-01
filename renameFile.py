import os

# specify the original file name and the new file name
original_file = str(input("Nama File Lama\t: ")).lower()
old = (f"{original_file}.text")
new_file = str(input("Nama File Ganti\t: ")).lower()
new = (f"{new_file}.text")

# rename the file
os.rename(old, new)

if new_file == original_file:
    print("Rename Failed!")
else:
    print("Rename Succesfully")