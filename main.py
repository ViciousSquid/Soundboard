print("*** Soundboard Starting up...")
print(" ")
print("LOG: Loading libraries...")

from soundboard_app import SoundboardApp

if __name__ == "__main__":
    app = SoundboardApp()
    app.mainloop()