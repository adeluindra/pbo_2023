from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmKerucut:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        
        # Pasang Label
        Label(mainFrame, text='Jari-jari Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Tinggi:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Luas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Volume:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        # Pasang Textbox
        self.txtJarijari = Entry(mainFrame) 
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)  

        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)  

        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5) 
        
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # Fungsi "onHitung" berfungsi untuk menghitung luas dan volume kerucut
    def onHitung(self, event=None):
        jarijari = float(self.txtJarijari.get())
        tinggi = float(self.txtTinggi.get())

        # Menghitung luas kerucut
        luas = math.pi * jarijari * (jarijari + math.sqrt(jarijari**2 + tinggi**2))

        # Menghitung volume kerucut
        volume = (1/3) * math.pi * jarijari**2 * tinggi

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmKerucut(root, "Program Luas dan Volume Kerucut")
    root.mainloop()
