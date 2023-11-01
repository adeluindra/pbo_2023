#kubus
print('menghitung luas dan volume kubus')

#variable
sisi = float(input('masukan sisi : '))

#rumus
luas = 6 * sisi * sisi
volume = sisi * sisi * sisi

#output
print('jumlah dari sisi : ', luas)
print('volume dari kubus : ', volume)











from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LuasVolumeKubus:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Sisi:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.txtSisi = Entry(mainFrame)
        self.txtSisi.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung Luas', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume', command=self.onHitungVolume)
        self.btnHitungVolume.grid(row=3, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        sisi = float(self.txtSisi.get())
        sisi = float(self.txtSisi.get())
        luas = 6 * sisi * sisi
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungVolume(self, event=None):
        sisi = float(self.txtSisi.get())
        sisi = float(self.txtSisi.get())
        sisi = float(self.txtSisi.get())
        Volume = sisi * sisi * sisi
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(Volume))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasVolumeKubus(root, "Menghitung Luas dan Volume Kubus")
    root.mainloop()