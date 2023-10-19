
#tabung
print('menghitung luas dan volume tabung')

#variable
oi = 22/7
jari_jari = float(input('masukan jari jari : '))
tinggi = float(input('masukan tinggi : '))

#rumus
luas = 2*oi*jari_jari*(jari_jari+tinggi)
volume = oi*jari_jari*jari_jari*tinggi

#output
print('luas permukaan tabung : ', luas)
print('volume tabung : ', volume)