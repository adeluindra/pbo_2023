import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    r = float(txtjari.get())

    from math import pi

    L = round (4 * pi * r * r,2)

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    r = float(txtjari.get())

    from math import pi

    V = round (4/3) * pi *(r**3)

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk.Tk()
app.title("kalkulator Luas Permukaan dan Volume Bola")

Frame = Frame(app)
Frame.pack(padx=30, pady=30)

nama = Label(Frame, text="Bola:")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=10)

jari = Label(Frame, text="jari jari:")
jari.grid(row=1, column=0, sticky=W, padx=5, pady=10)

txtjari = Entry(Frame)
txtjari.grid(row=1, column=1)

hitung_button = Button(Frame, text="Hitung", command=hitung, bg="cyan")
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

Luas = Label(Frame, text="Luas Permukaan: ")
Luas.grid(row=5, column=0, sticky=W, padx=5, pady=10)

volume = Label(Frame, text="Volume: ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=20)

txtluas = Entry(Frame)
txtluas.grid(row=5, column=1)

txtvolume = Entry(Frame)
txtvolume.grid(row=6, column=1)


app.mainloop()

