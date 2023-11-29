import tkinter as tk
from tkinter import filedialog
from pygame import mixer

def play_sound():
    mixer.init()
    mixer.music.load(selected_file.get())
    mixer.music.play()

def stop_sound():
    mixer.music.stop()

def choose_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        selected_file.set(file_path)

# Create the main window
window = tk.Tk()
window.title("Music Player")
window.geometry("400x250")
window.resizable(False, False)
window.configure(bg="cyan")

# Variable to store the selected music file path
selected_file = tk.StringVar()

# Create a label for the title
title_label = tk.Label(window, text="MOH SYAFIQ ADE LUWINDRA", font=("Helvetica", 10, 'bold'), bg="cyan")
title_label.pack(pady=2)

title_label = tk.Label(window, text="Music Player", font=("Helvetica", 20, 'bold'), bg="cyan", fg="Black")
title_label.pack(pady=10)

# Create a button to choose music
choose_button = tk.Button(window, text="Select Music", command=choose_music, bg="#4CAF50", fg="white")
choose_button.pack(pady=5)

# Create a label to display the selected music file
selected_label = tk.Label(window, textvariable=selected_file, bg="cyan", fg="black")
selected_label.pack(pady=5)

# Create a button to play the sound
play_button = tk.Button(window, text="Play", command=play_sound, bg="#2196F3", fg="white")
play_button.pack(pady=10)

# Create a button to stop the sound
stop_button = tk.Button(window, text="Stop", command=stop_sound, bg="#FF0000", fg="white")
stop_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
