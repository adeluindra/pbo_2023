class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_Reamur(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = (5/4) * float(self.suhu)
        return val
    
    def get_fahrenheit(self):
        val = (9/4 * float(self.suhu)) + 32
        return val

    def get_kelvin(self):
        val = (5/4 * float(suhu)) + 273.15
        return val

suhu = input("Masukan suhu dalam Reamur:")
R = Reamur(float(suhu))
val = R.get_Reamur()

C = R.get_celcius()
F = R.get_fahrenheit()
K = R.get_kelvin()

print(str(val) + " Reamur, sama dengan:")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")


