class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_kelvin(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = float(self.suhu) - 273.15
        return val
    
    def get_reamur(self):
        val = (4/5) * (float(self.suhu) - 273.15)
        return val

    def get_fahrenheit(self):
        val = (9/5 * (float(self.suhu) - 273.15)) + 32
        return val

suhu = input("Masukan suhu dalam Kelvin:")
K = Kelvin(float(suhu))
val = K.get_kelvin()

C = K.get_celcius()
R = K.get_reamur()
F = K.get_fahrenheit()

print(str(val) + " Kelvin, sama dengan:")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")


