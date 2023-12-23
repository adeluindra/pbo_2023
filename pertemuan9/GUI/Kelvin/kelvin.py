import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def get_celcius():
    suhu = txtsuhu.get()
    C = float(suhu) - 273.15
    txtFahrenheit.delete(0,END)
    txtFahrenheit.insert(END,C)

def get_reamur():
    suhu = txtsuhu.get()
    R = (4/5) * (float(suhu) - 273.15)
    txtReamur.delete(0,END)
    txtReamur.insert(END,R)

def get_fahrenheit():
    suhu = txtsuhu.get()
    F = (9/5 * (float(suhu) - 273.15)) + 32
    txtKelvin.delete(0,END)
    txtKelvin.insert(END,F)

def hitung():
    get_celcius()
    get_reamur()
    get_fahrenheit()

app = tk.Tk()

app.title("Kalkulator Suhu Kelvin")

frame = Frame(app)
frame.pack(padx=20, pady=20)

suhu= Label(frame, text="Kelvin:")
suhu.grid(row=0, column=0, sticky=W, padx=5, pady=5)

txtsuhu = Entry(frame)
txtsuhu.grid(row=0, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

F= Label(frame, text="Celcius:")
F.grid(row=3, column=0, sticky=W, padx=5, pady=5)

R= Label(frame, text="Reamur:")
R.grid(row=4, column=0, sticky=W, padx=5, pady=5)

K= Label(frame, text="Fahrenheit:")
K.grid(row=5, column=0, sticky=W, padx=5, pady=5)

txtFahrenheit = Entry(frame)
txtFahrenheit.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtReamur = Entry(frame)
txtReamur.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtKelvin = Entry(frame)
txtKelvin.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()