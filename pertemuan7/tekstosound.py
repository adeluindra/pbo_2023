import tkinter as tk
from gtts import gTTS
import pygame
import io

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech Converter")
        self.master.configure(bg='cyan')

        
        self.label = tk.Label(master, text="MOH SYAFIQ ADE LUWINDRA", font=("Helvetica", 10, 'bold'), bg="cyan")
        self.label.pack(pady=5)

        self.label = tk.Label(master, text="Masukkan teks:", bg='white')
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=10)

        self.button_convert = tk.Button(master, text="Convert", command=self.convert_text, bg="#4CAF50", fg="white")
        self.button_convert.pack(pady=10)

    def convert_text(self):
        input_text = self.text_entry.get()
        if input_text:
            language = 'ja'
            tts_object = gTTS(text=input_text, lang=language, slow=False)
            
            # Menggunakan Pygame untuk memainkan audio
            audio_file = io.BytesIO()
            tts_object.write_to_fp(audio_file)
            audio_file.seek(0)
            
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            
            # Tunggu hingga audio selesai
            while pygame.mixer.music.get_busy():
                continue
        else:
            tk.messagebox.showwarning("Peringatan", "Masukkan teks terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
