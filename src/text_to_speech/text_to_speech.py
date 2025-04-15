from gibberish_tts import TTSEngine

class TextToSpeechV1:
    def __init__(self):
        self.engine = TTSEngine()

    def load_speech(self, text : str) -> None:
        self.engine.load(text)

    def play_speech(self) -> None:
        self.engine.play()