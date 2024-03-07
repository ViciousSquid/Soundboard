
'''
Current version is 1.0
'''
print(" +++ Soundboard by Vicious Squid")
print("Importing libraries...")

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from tkinter import messagebox
import pygame.mixer
import os
import ctypes

class Application(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Soundboard")
        self.audio_manager = AudioManager()
        self.buttons = []
      
        # Create the button grid         
        for i in range(8):
            row = int(i / 4)
            column = i % 4
            button = Button(self, self.audio_manager)
            button.grid(row=row, column=column, padx=10, pady=10)
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

            # Choose an audio file and load it onto a button
    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 File", "*.mp3"),("WAV File", "*.wav")])
        if file_path:
            self.audio_manager.load_audio(file_path)
            audio_name = os.path.basename(file_path)
            self.buttons[len(self.audio_manager.audio_files) - 1].set_audio(len(self.audio_manager.audio_files) - 1, audio_name)

              # This box exists to help with official internal versioning - please don't remove it x
    def show_about_info(self):
            messagebox.showinfo(title="Soundboard", message="Version 1.0       https://github.com/ViciousSquid/Soundboard")


class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.audio_files = []
        self.muted = False
    def load_audio(self, file_path):
        audio = pygame.mixer.Sound(file_path)
        self.audio_files.append(audio)
        print("Debug: File loaded")
    def play_audio(self, index):
        if not self.muted:
            self.audio_files[index].play()
    def toggle_mute(self):
        self.muted = not self.muted

# Define the 'Button' class and make it beautiful

class Button(tk.Button):

    def __init__(self, master, audio_manager):
        super().__init__(master, text="Empty", command=self.play_audio, bg='tomato')
        self['font'] = ("Arial", 12)
        self['height'] = 4
        self['width'] = 25
        self.audio_manager = audio_manager
        self.audio_index = None
    def play_audio(self):
        if self.audio_index is not None:
            self.audio_manager.play_audio(self.audio_index)
    def set_audio(self, audio_index, audio_name):
        self.audio_index = audio_index
        self.config(text=audio_name)

if __name__ == "__main__":
    app = Application()
    app.mainloop()


