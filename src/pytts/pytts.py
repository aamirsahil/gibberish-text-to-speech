import pyttsx3

class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()

    def load(self, text : str) -> None:
        self.engine.say(text)

    def play(self) -> None:
        self.engine.runAndWait()