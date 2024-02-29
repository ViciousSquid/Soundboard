'''
Current version 0.19
'''
print(" +++ Soundboard by Vicious Squid")
print("Importing libraries...")

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import ctypes
from audio_manager import AudioManager
from button import Button

class Application(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Soundboard")
        self.audio_manager = AudioManager()
        self.buttons = []
      
        # Create the button grid
        for i in range(4):
            button = Button(self, self.audio_manager)
            button.grid(row=0, column=i, padx=10, pady=10)
            self.buttons.append(button)
            
        for i in range(4):
            button = Button(self, self.audio_manager)
            button.grid(row=1, column=i, padx=10, pady=10)
            self.buttons.append(button)

            # Menus
            menu = ttk.Menu(self)
            self.config(menu=menu)
            file_menu = ttk.Menu(menu)
            menu.add_cascade(label="File", menu=file_menu)
            file_menu.add_command(label="Load Audio", command=self.load_audio)
            help_menu = ttk.Menu(menu)
            menu.add_cascade(label="Help", menu=help_menu)
            help_menu.add_command(label="About", command=self.show_about_info)  

            # Logic for file management and updating the button names
            # Refer also to audio_manager.py

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 File", "*.mp3"),("WAV File", "*.wav")])
        if file_path:
            self.audio_manager.load_audio(file_path)
            audio_name = os.path.basename(file_path)
            self.buttons[len(self.audio_manager.audio_files) - 1].set_audio(len(self.audio_manager.audio_files) - 1, audio_name)

              # This box exists to help with official internal versioning
    def show_about_info(self):
            messagebox.showinfo(title="Soundboard", message="Version 0.19       https://github.com/ViciousSquid/Soundboard")

    def toggle_mute(self):
        mixer.music.stop()
if __name__ == "__main__":
    app = Application()
    app.mainloop()

