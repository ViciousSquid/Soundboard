import os
import tkinter as tk
from tkinter import filedialog, messagebox
from audio_manager import AudioManager
from sound_button import SoundButton

class SoundboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Soundboard")
        self.audio_manager = AudioManager()
        self.create_menu()
        self.create_buttons()

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Audio", command=self.load_audio)

        help_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_buttons(self):
        self.buttons = []
        for i in range(8):
            row = i // 4
            col = i % 4
            button = SoundButton(self, self.audio_manager, text="Empty")
            button.grid(row=row, column=col, padx=10, pady=10)
            self.buttons.append(button)

    def load_audio(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )
        if file_path:
            try:
                self.audio_manager.load_audio(file_path)
                audio_name = os.path.basename(file_path)
                for button in self.buttons:
                    if button.audio_path is None:
                        button.set_audio(file_path, audio_name)
                        break
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def show_about(self):
        messagebox.showinfo(
            title="Soundboard",
            message="Version 1.2\nhttps://github.com/ViciousSquid/Soundboard",
        )