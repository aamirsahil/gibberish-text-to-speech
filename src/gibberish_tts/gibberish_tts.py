from typing import List, Dict

class TTSEngine():
    def __init__(self):
        pass

    def load(self, text : str) -> None:
        text_pieces = self.divideToPieces(text)
        audio_pieces = self.findAudio(text_pieces)
        audio_pieces = self.modifyAudio(audio_pieces)

    def divideToPieces(self, text : str) -> List[str]:
        text_pieces = text.split()
        return text_pieces
    
    def findAudio(self, text_pieces : List[str]) -> List[Dict]:
        pass

    def modifyAudio(self, audio_pieces : List[Dict]) -> List[Dict]:
        pass

    def play(self) -> None:
        pass