import tkinter as tk
from tkinter import Frame, Label, Entry, Button,END, W
from math import pi


def hitung_volume():
    r = float(txtjari.get())
    T = float(txttinggi.get())

    V = round(pi*r*r*T, 2)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung_luaspermukaan():
    r = float(txtjari.get())
    T = float(txttinggi.get())
    
    lp = round(2*pi*r*(T + r),2)
    
    txtluaspermukaan.delete(0,END)
    txtluaspermukaan.insert(END,lp)

def hitung():
    hitung_volume()
    hitung_luaspermukaan()
    
app = tk.Tk()
app.title("Program Menghitung volume dan luas permukaan")

Frame = Frame(app)
Frame.pack(padx=30, pady=30)

name = Label(Frame, text='Tabung: ')
name.grid(row=0, column=0, sticky=W, padx=5, pady=5)

jari = Label(Frame, text='Jari - Jari: ')
jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

tinggi = Label(Frame, text='Tinggi: ')
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

volume = Label(Frame, text='Volume: ')
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

lp = Label(Frame, text='Luas Permukaan: ')
lp.grid(row=6, column=0, sticky=W, padx=5, pady=5)

hitung_button = Button(Frame, text="Hitung Volume", command = hitung_volume, bg = 'cyan')
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

hitunglp_button = Button(Frame, text="Hitung Luas permukaan", command = hitung_luaspermukaan, bg = 'cyan')
hitunglp_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtjari = Entry(Frame)
txtjari.grid(row=1, column=1)

txttinggi = Entry(Frame)
txttinggi.grid(row=2, column=1)

txtvolume = Entry(Frame)
txtvolume.grid(row=5, column=1)

txtluaspermukaan = Entry(Frame)
txtluaspermukaan.grid(row=6, column=1)

nama = Label(Frame, text=' ')
nama.grid(row=7, column=0, sticky=W, padx=5, pady=5)

app.mainloop()
