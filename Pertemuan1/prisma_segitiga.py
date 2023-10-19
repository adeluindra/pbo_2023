#prisma segitiga
print('menghitung luas dan volume prisma segitiga')

#variable
keliling_segitiga = float(input('masukan Keliling Segitiga : '))
tinggi_prisma = float(input('masukan Tinggi prisma : '))
luas_segitiga = float(input('masukan Luas segitiga : '))

#rumus
luas1 = keliling_segitiga * tinggi_prisma
luas2 = keliling_segitiga * tinggi_prisma * luas_segitiga
volume = 1/2 * luas_segitiga * tinggi_prisma

#output
print('jumlah dari sisi : ', luas1)
print('jumlah dari sisi : ', luas2)
print('volume dari limas segiempat : ', volume)