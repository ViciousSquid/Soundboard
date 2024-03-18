# keyboard_shortcut_handler.py
# version 1.22.10

class KeyboardShortcutHandler:
    def __init__(self, master):
        self.master = master
        self.shortcuts = {}

        # Bind the key press event to the master window
        self.master.bind("<Key>", self.handle_key_press)

    def register_shortcut(self, button, shortcut_key):
        self.shortcuts[shortcut_key] = button

    def handle_key_press(self, event):
        pressed_key = event.keysym
        if pressed_key in self.shortcuts:
            button = self.shortcuts[pressed_key]
            button.play_audio()