'''
This file contains the AudioManager class responsible for loading and playing audio files.
'''
import pygame.mixer
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