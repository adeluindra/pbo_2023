import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())

    L = pj * lb

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_keliling():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())

    K = 2 * (pj + lb)

    txtkeliling.delete(0,END)
    txtkeliling.insert(END,K)

def hitung():
    hitung_luas()
    hitung_keliling()

app = tk.Tk()
app.title("kalkulator Menghitung Luas dan Volume ")

Frame = Frame(app)
Frame.pack(padx=30, pady=30)

nama = Label(Frame, text="PERSEGI PANJANG:")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=10)

panjang = Label(Frame, text="panjang:")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=10)

lebar = Label(Frame, text="lebar:")
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=10)

txtpanjang = Entry(Frame)
txtpanjang.grid(row=1, column=1)

txtlebar = Entry(Frame)
txtlebar.grid(row=2, column=1)

hitung_button = Button(Frame, text="Hitung", command=hitung,bg='cyan') 
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

Luas = Label(Frame, text="Luas: ")
Luas.grid(row=4, column=0, sticky=W, padx=5, pady=10)

Keliling = Label(Frame, text="Keliling: ")
Keliling.grid(row=5, column=0, sticky=W, padx=5, pady=20)

txtluas = Entry(Frame)
txtluas.grid(row=4, column=1)

txtkeliling = Entry(Frame)
txtkeliling.grid(row=5, column=1)


app.mainloop()

