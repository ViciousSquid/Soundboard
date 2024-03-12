import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.audio_files = []
        self.muted = False

    def load_audio(self, file_path):
        try:
            audio = pygame.mixer.Sound(file_path)
            self.audio_files.append(audio)
            print(f"Loaded audio file: {file_path}")
        except pygame.error as e:
            print(f"Error loading audio file: {e}")

    def play_audio(self, index):
        if not self.muted and 0 <= index < len(self.audio_files):
            self.audio_files[index].play()

    def toggle_mute(self):
        self.muted = not self.muted