from typing import List, Dict

class TTSEngine():
    def __init__(self):
        pass

    def _findAudioFile(self, text_element : str) -> str:
        pass

    def load(self, text : str) -> None:
        text_list = self.textDivide(text)
        audio_list = self.findAudio(text_list)
        audio_list = self.modifyAudio(audio_list)

    def textDivide(self, text : str) -> List[str]:
        text_list = text.split()
        return text_list
    
    def findAudio(self, text_list : List[str]) -> List[Dict]:
        audio_list = []
        for text_element in text_list:
            audio_list.append({})
            audio_list[-1]['file_name'] = self._findAudioFile(text_element)

    def modifyAudio(self, audio_list : List[Dict]) -> List[Dict]:
        pass

    def play(self) -> None:
        pass