import tkinter as tk
from tkinter import messagebox, filedialog, W

def simpan_jadwal():
    hari = entry_hari.get()
    waktu = entry_waktu.get()
    mata_kuliah = entry_mata_kuliah.get()
    
    jadwal = f"{hari}: {waktu} - {mata_kuliah}\n"
    
    with open("jadwal_kuliah.txt", "a") as file:
        file.write(jadwal)
    
    entry_hari.delete(0, "end")
    entry_waktu.delete(0, "end")
    entry_mata_kuliah.delete(0, "end")
    messagebox.showinfo("Info", "Jadwal berhasil disimpan!")

def tampilkan_jadwal():
    with open("jadwal_kuliah.txt", "r") as file:
        jadwal = file.read()
    
    messagebox.showinfo("Jadwal Kuliah", jadwal)

def buka_file_jadwa():
    file_name = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
    if file_name:
        with open(file_name, 'r') as file:
            jadwal = file.read()
        messagebox.showinfo('Jadwal Kuliah', jadwal)

root = tk.Tk()
root.title("Aplikasi Jadwal Kuliah")

frame = tk.Frame(root, bg='cyan')
frame.pack(pady=20)

name = tk.Label(frame, text='Moh Syafiq Ade Luwindra', bg='cyan')
label_hari = tk.Label(frame, text="Hari :", bg='cyan')
label_waktu = tk.Label(frame, text="Waktu :", bg='cyan')
label_mata_kuliah = tk.Label(frame, text="Mata Kuliah :", bg='cyan')

entry_hari = tk.Entry(frame)
entry_waktu = tk.Entry(frame)
entry_mata_kuliah = tk.Entry(frame)

name.grid(row=0, column=0, sticky=W, padx=5, pady=5)
label_hari.grid(row=1, column=0, sticky=W, padx=5, pady=5)
entry_hari.grid(row=1, column=2, sticky=W, padx=5, pady=5)
label_waktu.grid(row=2, column=0, sticky=W, padx=5, pady=5)
entry_waktu.grid(row=2, column=2, sticky=W, padx=5, pady=10)
label_mata_kuliah.grid(row=3, column=0, sticky=W, padx=5, pady=5)
entry_mata_kuliah.grid(row=3, column=2, sticky=W, padx=5, pady=5)

button_simpan = tk.Button(frame, text="Simpan Jadwal", command=simpan_jadwal, bg='#4CAF50')
button_tampilkan = tk.Button(frame, text="Tampilkan Jadwal", command=tampilkan_jadwal, bg='#4CAF50')
button_buka = tk.Button(frame, text="Buka File Jadwal", command=buka_file_jadwa, bg='#4CAF50')

button_simpan.grid(row=4, column=0, pady=5)
button_tampilkan.grid(row=4, column=2, pady=5)
button_buka.grid(row=5, column=0, pady=5)

root.mainloop()
