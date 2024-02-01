import getpass
userid = 'ez'
passw = 'secret'

uid = input('masukan id anda : ')
pwd = getpass.getpass('masukan password anda : ')
if uid == userid and pwd == passw :
    print(f'Sukses Login..Selamat datang {userid}')
else :
    print('User ID atau password salah')