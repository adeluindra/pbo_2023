#kerucut
import math

print('menghitung luas dan volume kerucut')

#variable
oi = 22/7
tinggi = float(input('masukan tinggi : '))
jari_jari = float(input("Masukkan jari-jari bola: "))
tambahan = math.sqrt((jari_jari**2)+(tinggi*tinggi))

#rumus
luas = oi*jari_jari*(jari_jari+tambahan)
volume = 1/3*oi*(jari_jari**2)*tinggi

#output
print("Luas permukaan bola adalah:", luas)
print("Volume bola adalah:", volume)

