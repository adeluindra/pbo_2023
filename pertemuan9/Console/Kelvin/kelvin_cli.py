print("Konversi Suhu Kelvin")

suhu_kelvin = input("Masukkan suhu dalam Kelvin: ")

C = float(suhu_kelvin) - 273.15
R = (4/5) * (float(suhu_kelvin) - 273.15)
F = (9/5 * (float(suhu_kelvin) - 273.15)) + 32

print(suhu_kelvin + " Kelvin sama dengan ")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")
