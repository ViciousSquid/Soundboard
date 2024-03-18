# soundboard_app.py
# version 1.22.10

import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import tkinter.colorchooser as colorchooser
from audio_manager import AudioManager
from sound_button import SoundButton
from keyboard_shortcut_handler import KeyboardShortcutHandler

# Generate a random hex colour on startup
import random
random_number = random.randint(0,16777215)
hex_number = str(hex(random_number))
hex_number ='#'+ hex_number[2:]
# Debug Log it
print(" ")
print("LOG: Randomly generated hex colour: ", hex_number)

class SoundboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Soundboard")
        self.audio_manager = AudioManager()
        self.bar_color = hex_number # Apply the previously generated hex colour
        self.create_menu()

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)

        self.create_buttons()

        # Create an instance of KeyboardShortcutHandler
        self.shortcut_handler = KeyboardShortcutHandler(self)

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Audio", command=self.load_audio)

        settings_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Change Bar Colour", command=self.pick_color)
        settings_menu.add_command(label="Assign Shortcuts", command=self.assign_shortcuts)

        help_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        self.color_bar_frame = tk.Frame(self, height=5, bg=self.bar_color)
        self.color_bar_frame.pack(side=tk.TOP, fill=tk.X)

    def pick_color(self):
        new_color = colorchooser.askcolor(title="Choose Bar Colour")[1]
        if new_color:
            self.bar_color = new_color
            self.color_bar_frame.config(bg=new_color)

    def create_buttons(self):
        self.buttons = []
        for i in range(8):
            row = i // 4
            col = i % 4
            button = SoundButton(self.buttons_frame, self.audio_manager, text="Empty")
            button.grid(row=row, column=col, padx=10, pady=10)
            self.buttons.append(button)

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
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

    def assign_shortcuts(self):
        for button in self.buttons:
            if button.audio_path:
                shortcut_key = simpledialog.askstring(
                    "Assign Shortcut",
                    f"Enter a shortcut key for '{button['text']}':",
                    parent=self
                )
                if shortcut_key:
                    self.shortcut_handler.register_shortcut(button, shortcut_key)

    def show_about(self):
        messagebox.showinfo(title="Soundboard", message="Version 1.22.10\nhttps://github.com/ViciousSquid/Soundboard")