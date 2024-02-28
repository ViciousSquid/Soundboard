'''
Current version 0.17
'''
print(" +++ Soundboard by Vicious Squid")
print("https://github.com/ViciousSquid/Soundboard")
print("Importing libraries...")

import ttkbootstrap as ttk
from tkinter import filedialog
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
      
        # Top row of 4 buttons
        for i in range(4):
            button = Button(self, self.audio_manager)
            button.grid(row=0, column=i, padx=10, pady=10)
            self.buttons.append(button)
            # Bottom row of 4 buttons
        for i in range(4):
            button = Button(self, self.audio_manager)
            button.grid(row=1, column=i, padx=10, pady=10)
            self.buttons.append(button)

            # Create the File menu
            menu = ttk.Menu(self)
            self.config(menu=menu)
            file_menu = ttk.Menu(menu)
            menu.add_cascade(label="File", menu=file_menu)
            file_menu.add_command(label="Load Audio", command=self.load_audio)
        
          
    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 File", "*.mp3"),("WAV File", "*.wav")])
        if file_path:
            self.audio_manager.load_audio(file_path)
            audio_name = os.path.basename(file_path)
            self.buttons[len(self.audio_manager.audio_files) - 1].set_audio(len(self.audio_manager.audio_files) - 1, audio_name)
    def toggle_mute(self):
        mixer.music.stop()
if __name__ == "__main__":
    app = Application()
    app.mainloop()

