'''
This file defines the Button class, which represents a single button in the GUI.
'''
import tkinter as tk
class Button(tk.Button):
    def __init__(self, master, audio_manager):
        super().__init__(master, text="Empty", command=self.play_audio)
        self['font'] = ("Arial", 12)
        self.audio_manager = audio_manager
        self.audio_index = None
    def play_audio(self):
        if self.audio_index is not None:
            self.audio_manager.play_audio(self.audio_index)
    def set_audio(self, audio_index, audio_name):
        self.audio_index = audio_index
        self.config(text=audio_name)