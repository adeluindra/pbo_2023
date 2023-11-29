import cv2
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")
        self.master.configure(bg='yellow')

        self.style = ttk.Style()
        self.style.theme_use("clam")  # You can try other themes like "aquativo", "kroc", etc.

        self.cap = None
        self.is_playing = False

        # Create and style buttons
        self.title_label = ttk.Label(master, text="MOH SYAFIQ ADE LUWINDRA", font=("Helvetica", 10, "bold"), background="white")
        self.btn_open = ttk.Button(master, text="Open Video", command=self.open_file)
        self.btn_play = ttk.Button(master, text="Play", state=tk.DISABLED, command=self.play_video)
        self.btn_stop = ttk.Button(master, text="Stop", state=tk.DISABLED, command=self.stop_video)

        # Create and style labels
        self.video_label = ttk.Label(master)
        self.video_label.grid(row=2, column=0, columnspan=5, pady=10)

        # Grid layout
        self.btn_open.grid(row=1, column=1, padx=10, pady=10)
        self.btn_play.grid(row=1, column=2, padx=10, pady=10)
        self.btn_stop.grid(row=1, column=3, padx=10, pady=10)
        self.title_label.grid(row=0, column=0, columnspan=5, pady=5)
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
        if file_path:
            self.cap = cv2.VideoCapture(file_path)
            if self.cap.isOpened():
                self.btn_play.config(state=tk.NORMAL)
                self.btn_stop.config(state=tk.DISABLED)
                self.is_playing = False
            else:
                self.cap = None
                self.show_error("Error opening video file")

    def play_video(self):
        if self.cap is not None and not self.is_playing:
            self.is_playing = True
            self.btn_play.config(state=tk.DISABLED)
            self.btn_stop.config(state=tk.NORMAL)
            self.show_frame()

    def show_frame(self):
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = ImageTk.PhotoImage(img)
                self.video_label.img = img
                self.video_label.config(image=img)
                self.video_label.after(10, self.show_frame)
            else:
                self.stop_video()

    def stop_video(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        self.btn_play.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.is_playing = False

    def on_close(self):
        if self.cap is not None:
            self.cap.release()
        self.master.destroy()

    def show_error(self, message):
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()
