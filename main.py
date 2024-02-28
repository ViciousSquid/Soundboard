'''
Current version 0.16
'''
print(" +++ Soundboard by Rufus Pearce")
print("Importing libraries...")
import tkinter as tk
from tkinter import filedialog
import os
import ctypes
from audio_manager import AudioManager
from button import Button
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Soundboard")
        self.audio_manager = AudioManager()
        self.buttons = []
        # Create buttons
        for i in range(6):
            button = Button(self, self.audio_manager)
            button.grid(row=0, column=i, padx=10, pady=10)
            self.buttons.append(button)

        # Create menu
        menu = tk.Menu(self)
        self.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Audio", command=self.load_audio)

        # Create mute button
        # mute_button = tk.Button(self, text="Mute", command=self.toggle_mute)
        # mute_button.grid(row=1, column=0, padx=5, pady=5)
    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 File", "*.mp3"),("WAV File", "*.wav")])
        if file_path:
            self.audio_manager.load_audio(file_path)
            audio_name = os.path.basename(file_path)
            self.buttons[len(self.audio_manager.audio_files) - 1].set_audio(len(self.audio_manager.audio_files) - 1, audio_name)
    def toggle_mute(self):
        self.audio_manager.toggle_mute()
if __name__ == "__main__":
    app = Application()
    app.mainloop()

