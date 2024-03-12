import tkinter as tk
import threading

class SoundButton(tk.Button):
    def __init__(self, master, audio_manager, **kwargs):
        super().__init__(master, **kwargs)
        self.audio_manager = audio_manager
        self.audio_index = None
        self.config(
            font=("Arial", 12),
            height=4,
            width=25,
            bg="#91a0d9",  # Initial color
            command=self.play_audio,
        )

    def play_audio(self):
        if self.audio_index is not None:
            play_thread = threading.Thread(
                target=self.audio_manager.play_audio, args=(self.audio_index,)
            )
            play_thread.start()

    def set_audio(self, audio_index, audio_name):
        self.audio_index = audio_index
        self.config(text=audio_name, bg="#98fb98")  # Green color