# Episode 11 Memadukan list comprehension dan conditional if
# listmu = [30, 60, 10, 55]
# listku = {item for item in listmu if item > 50}
# print(f'listku{listmu}')
# print(f'listku{listku}')

# Episode 12 Memadukan list comprehesion dan fungsi zip
# nama = ['reyhan', 'ezra', 'bimantara']
# usia = ['23', '31', '26']
# listku = [[d_nama, d_usia]for d_nama, d_usia in zip(nama, usia)]
# print(f'listku:{listku}')

# Episode 13 Memotong list dan string (slicing)
# listmu = [10, 20, 30, 40, 60]
# listku = listmu[2:5]
# print(f'listku:{listku}')

# kata = "PEMBELAJARAN"
# print(kata[3:10])

# Episode 14 Membalikkan urutan list dan string
# listmu = [10, 20, 30, 40, 50, 60]
# listku = listmu[::-1]
# print(f'listku:{listku}')

# kata = 'BELAJAR'
# print(kata[::-1])

# Episode 15 Memecah sekumpulan kata dalam kalimat ke dalam list
# teks = 'belajar python dasar'
# listku = teks.split()
# print(f'listku:{listku}')

# Episode 16 Menggabungkan sekumpulan kata menjadi kalimat
# listku = ['belajar', 'python', 'dasar']
# kalimat = ' '.join(listku)
# print(f'kalimat:{kalimat}')

# Episode 17 Pemanggilan fungsi berantai
# def tambah(a, b):
#     return a + b

# def kali(a, b):
#     return a * b

# x, y = 10, 20
# kondisi = True
# hasil = (tambah if kondisi else kali)(x, y)
# print(f'hasil:{hasil}')

# Episode 18 Percabangan dengan dictionary (switch)
# def one():
#     print('satu-one')
# def two():
#     print('dua-two')
# def three():
#     print('tiga-three')

# case = 'dua'
# switch = {
#     'satu': one,
#     'dua': two,
#     'tiga': three
# }
# switch[case]()

# Episode 19 Penggabungan list
# a = [10, 20, 30]
# b = [40, 50, 60]
# c = a + b
# print(f'list c:{c}')

# Episode 20 Mengenal ekspresi tenary
# a = 10
# b = 'negatif' if a < 10 else 'positif'
# print(f'{a} bernilai {b}')

# Episode 21 Mengabaikan nilai dengan underscore
# listku = [10, 20, 30, 40, 50]
# *_, a, b = listku
# print(f'listku:{listku}')
# print(f'a:{a}, b:{b}')

# Episode 22 Mengenal operator IN untuk memerikasa keberadaan seuatu nilai list
# listku = [10, 20, 30, 40, 50]
# cari = 30
# ketemu = False
# if cari in listku:
#     print('ketemu')
# else:
#     print('tidak ketemu')

# Episode 23 Membuat fungsi dengan sekumpulan nilai kembalian
# def fungsiku():
#     nim = '036'
#     nama = 'Ezra'
#     ipk = 1.25
#     return nim, nama, ipk
# a, b, c = fungsiku()
# print(f'a:{a}')
# print(f'b:{b}')
# print(f'c:{c}')

# Episode 24 Mengenal fungsi zip untuk menyatukan sekumpulan list yang berkolerasi
# nim = ['001', '002', '003']
# nama = ['reyhan', 'ezra', 'bimantara']
# ipk = [3.25, 2.33, 1.88]
# siswa = list(zip(nim, nama, ipk))
# print(f'siswa:{siswa}')

# Episode 25 Mengenal fungsi unzip untuk memecah sekumpulan nilai pada list
# siswa = [('001', 'bejo', 3.25),
#          ('002', 'karti', 2.33),
#          ('003', 'tejo', 1.88)]
# nim, nama, ipk = zip(*siswa)
# print(f'nim:{nim}')
# print(f'nama:{nama}')
# print(f'ipk:{ipk}')

# Episode 26 Mengenal sumber dadya (resources) dengan context manager
# with open('pesan.txt', 'w') as fileku:
#     fileku.write('Semangat belajar pyhtonic \n')
#     fileku.write('Bersama Indonesia Belajar \n')

# Episode 27 Mengenal method count list untuk menghitung jumlah kemunculan suatu nilai
# listku = [30, 20, 60, 20, 10, 30, 20]
# hitung = 20
# jumlah = listku.count(hitung)
# print(f'ditemukan:{jumlah}')

# Episode 28 Mengenal format teks (string formatting)
# nama = 'bejo'
# usia = 25
# print('nama saya ' + nama + ' usia saya ' + str(usia) + ' tahun')
# print('nama saya %s usia saya %d tahun' % (nama, usia))
# print('nama saya {} usia saya {} tahun'.format(nama, usia))
# print('nama saya {1} usia saya {0} tahun'.format(usia, nama))
# siswa = {
#     'nim': '001',
#     'nama': 'tejo',
#     'usia': 35,
#     'ipk': 3.75
# }
# print('nama saya {nama} usia saya {usia}'.format(**siswa))
# print(f'nama saya {nama}, usia saya {usia}')

# Episode 29 Menggabungkan/ menyatukan dictionary
# data1 = {
#     'nim': '001',
#     'nama': 'bejo'
# }
# data2 = {
#     'ipk': 3.25,
#     'semester': 4
# }
# data3 = {
#     'kota': 'Palembang',
#     'hobi': 'Ngoding'
# }
# siswa = {**data1, **data2, **data3}
# print(f'siswa:{siswa}')

# Episode 30 Menggantikan operator OR dengan operator IN
# nama = 'bejo'
# if nama in ('bejo', 'tejo', 'karti'):
#     print('siswa teladan')
# else:
#     print('siswa reguler')

# Episode 31 Mengenal Else pada perulangan for loop
# kecepatan = [60, 40, 80, 60, 90, 30, 110, 20]
# ambang_batas = 100
# for laju in kecepatan:
#     if laju > ambang_batas:
#         laju_normal = False
#         print('Kecepatan melampaui ambang batas')
#         break
# else:
#     print('laju kendaraan normal')

# Episode 32 Penanda posisi digit (digit placeholder)
# gaji = 50_000_000
# print(f'gaji:{gaji}')

# Episode 33 Mengenal tabel translasi
# sumber = 'aieo'
# tujuan = '4130'
# string_input = 'kota cirebon'
# tabel_translasi = str.maketrans(sumber, tujuan)
# string_output = string_input.translate(tabel_translasi)
# print(f'hasil konversi:{string_output}') 

# Episode 34 Pengurutan data dengan method sort dan fungsi sorted
# siswa = ['karti susanti', 'tejo purnawan', 'bejo rahmadi']
# terurut = sorted(siswa)
# print(terurut)

# Episode 35 Pengurutan data dengan custom key pada fungsi sorted
# def custom_key(nama):
#     return nama.split()[-1]
# siswa = ['karti susanti', 'tejo purnawan', 'bejo rahmadi']
# # terurut = sorted(siswa, key = custom_key)
# terurut = sorted(siswa, key = lambda x: x.split()[-1])
# print(f'terurut:{terurut}')

# Episode 36 Mengenal multiple assignment untuk meringkat inisiasi variabel
# a = b = c = 10
# print(f'{a} {b} {c}')

# Episode 37 Mengenal keyword argument dan positional arguments
# def cetak_nama(f_name, l_name):
#     print(f'{f_name} {l_name}')
# cetak_nama(f_name='San', l_name='Susanti')

# Episode 38 Melakukan unpacking argument pada pemanggilan fungsi
# def jumlahkan(p_1, p_2):
#     return p_1 + p_2
# listku = [10, 20]
# dictku = {
#     'p_1': 100,
#     'p_2': 200
# }

# hasil_list = jumlahkan(*listku)
# print(f'hasil list:{hasil_list}')
# hasil_dict = jumlahkan(**dictku)
# print(f'hasil dict:{hasil_dict}')

# Episode 39 Mengenal dan merangkai beberapa method string
# x = '   bahasa pemrograman python: guido van rossum   '
# print(f'x:{x}')
# y = x.strip().upper().replace(':',';')
# print(f'y:{y}')

# Episode 40 Mengenal defaul argument (function overloading)
# def salam(nama, pesan = ''):
#     print(f'Hai {nama}! {pesan}')
# salam('Ezra', 'selamat malam')