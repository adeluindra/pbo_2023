from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmLimasSegitiga:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Pasang Label
        Label(mainFrame, text='Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Tinggi Alas:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Tinggi Limas:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # Pasang Textbox
        self.txtAlas = Entry(mainFrame) 
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)  

        self.txtTinggiAlas = Entry(mainFrame) 
        self.txtTinggiAlas.grid(row=1, column=1, padx=5, pady=5)

        self.txtTinggiLimas = Entry(mainFrame) 
        self.txtTinggiLimas.grid(row=2, column=1, padx=5, pady=5) 
        
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung, bg='cyan')
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # Fungsi "onHitung" berfungsi untuk menghitung luas dan volume limas segitiga
    def onHitung(self, event=None):
        alas = float(self.txtAlas.get())
        tinggi_alas = float(self.txtTinggiAlas.get())
        tinggi_limas = float(self.txtTinggiLimas.get())

        luas = (alas * tinggi_limas) / 2
        volume = (1/3) * alas * tinggi_alas * tinggi_limas

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasSegitiga(root, "Program Luas dan Volume Limas Segitiga")
    root.mainloop()
    