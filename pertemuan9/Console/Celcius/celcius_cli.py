print("Konversi Suhu Celcius")

suhu = input("Masukan suhu dalam celcius:")

F = (9/5 * float(suhu)) + 32
R = (4/5 * float(suhu))
K = float(suhu) + 32

print(suhu + " Celcius sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")