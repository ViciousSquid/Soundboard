import pygame
from collections import defaultdict

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.audio_files = defaultdict(lambda: None)
        self.muted = False

    def __del__(self):
        pygame.mixer.quit()

    def load_audio(self, file_path):
        try:
            audio = pygame.mixer.Sound(file_path)
            self.audio_files[file_path] = audio
            print(f"Loaded audio file: {file_path}")
        except pygame.error as e:
            print(f"Error loading audio file: {e}")

    def play_audio(self, file_path):
        if not self.muted and file_path in self.audio_files:
            self.audio_files[file_path].play()

    def toggle_mute(self):
        self.muted = not self.muted