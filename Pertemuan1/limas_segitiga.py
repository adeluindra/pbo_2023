#limas segitiga
print('menghitung luas dan volume limas segi empat')

#variable
sisi = float(input('masukan jumlah sisi : '))
la = float(input('masukan luas alas : '))
tinggi = float(input('masukan tinggi : '))

#rumus
luas = la + sisi
volume = 1/3 * (1/2 * la * tinggi)

#output
print('luas dari limas segitiga : ', luas)
print('volume dari limas segiempat : ', volume)