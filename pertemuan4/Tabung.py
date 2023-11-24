from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmSilinderTabung:
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

        Label(mainFrame, text='Tinggi Tabung:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Luas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Volume:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        # Pasang Textbox
        self.txtJarijariAlas = Entry(mainFrame) 
        self.txtJarijariAlas.grid(row=0, column=1, padx=5, pady=5)  

        self.txtTinggiTabung = Entry(mainFrame) 
        self.txtTinggiTabung.grid(row=1, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5) 
        
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung, bg='cyan')
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # Fungsi "onHitung" berfungsi untuk menghitung luas dan volume silinder/tabung
    def onHitung(self, event=None):
        jarijari_alas = float(self.txtJarijariAlas.get())
        tinggi_tabung = float(self.txtTinggiTabung.get())

        luas = 2 * math.pi * jarijari_alas * (jarijari_alas + tinggi_tabung)
        volume = math.pi * jarijari_alas**2 * tinggi_tabung

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmSilinderTabung(root, "Program Luas dan Volume Silinder/Tabung")
    root.mainloop()
