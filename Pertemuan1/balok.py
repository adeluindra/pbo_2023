#balok
print('menghitung luas dan volume balok')

#variable
panjang = float(input('masukan panjang : '))
lebar = float(input('masukan lebar : '))
tinggi = float(input('masukan tinggi : '))

#rumus
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
volume = panjang * lebar * tinggi

#output
print('jumlah dari sisi : ', luas)
print('volume dari kubus : ', volume)


