import tkinter as tk
from tkinter import Menu
from FrmPersegi import *
from FrmSegitiga import *
from FrmLingkaran import *
from Balok import *
from Bola import *
from Kerucut import *
from LimasSegiEmpat import *
from Kubus import *
from FrmTranslator import *
from LimasSegiTiga import *
from PersegiPanjang import *
from Tabung import *
from PrismaSegitiga import *



# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)
tranlator_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Persegi', command= lambda: new_window("Luas Persegi", FrmPersegi)
)
app_menu.add_command(
    label='App Segitiga', command= lambda: new_window("Luas Segitiga", FrmSegitiga)
)
app_menu.add_command(
    label='App Lingkaran', command= lambda: new_window("Luas Lingkaran", FrmLingkaran)
)
app_menu.add_command(
    label='App Balok', command= lambda: new_window("Luas Balok", FrmBalok)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Luas Bola", FrmBola)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Luas Kerucut", FrmKerucut)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Luas Kubus", FrmKubus)
)
app_menu.add_command(
    label='App Limas SegiTiga', command= lambda: new_window("Luas Limas SegiTiga", FrmLimasSegitiga)
)
app_menu.add_command(
    label='App Persegi Panjang', command= lambda: new_window("Luas Persegi Panjang", FrmPersegiPanjang)
)
app_menu.add_command(
    label='App Limas Segi Empat', command= lambda: new_window("Luas Limas SegiEmpat", FrmLimasSegiEmpat)
)
app_menu.add_command(
    label='App Limas Silinder Tabung', command= lambda: new_window("Luas Limas Silinder Tabung", FrmSilinderTabung)
)
app_menu.add_command(
    label='App Prisma Segitiga', command= lambda: new_window("Luas Prisma Segitiga", FrmPrismaSegitiga)
)
tranlator_menu.add_command(
    label='App Tranlate', command= lambda: new_window("Translate", FrmTranslator)
)



def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
menubar.add_cascade(
    label="Translate", menu=tranlator_menu
)
    
root.mainloop()