from typing import List, Dict
import librosa
import sounddevice as sd
import numpy as np


class TTSEngine():
    def __init__(self):
        self.audio_data = []
        self.sr = 0
        self.playback_speed = 3

        self.pause_duration = np.random.randint(1000, 5000)
        self.pitch_shift = np.random.randint(-12, 12)
        self.pause_array = np.zeros(self.pause_duration)

        self.audio_path_root = "./src/assets/sound_files/alphabets/"

    def load(self, text : str) -> None:
        text_list = self._textDivide(text)
        audio_list = self._findAudio(text_list)
        self._combineAudio(audio_list)
        self._modifyAudio()

    def play(self) -> None:
        sd.play(self.audio_data, self.sr)
        sd.wait()

    def _findAudioFile(self, text : str) -> str:
        if text == " ":
            return "<|space|>"
        return self.audio_path_root + text + '.wav'

    def _findAudio(self, text_list : List[str]) -> List[Dict]:
        audio_list = []
        for text in text_list:
            audio_list.append({})
            audio_list[-1]['file_name'] = self._findAudioFile(text)

        return audio_list

    def _textDivide(self, text : str) -> List[str]:
        text_list = list(text)
        return text_list
    
    def _combineAudio(self, audio_list : List):
        for audio in audio_list:
            if audio['file_name'] == "<|space|>":
                self.audio_data.append(self.pause_array)
                continue
            filename = audio['file_name']
            data, sr = librosa.load(filename, sr=None)
            self.audio_data.append(data)
        self.sr = sr
        self.audio_data = np.concatenate(self.audio_data)

    def _modifyAudio(self):
        self.audio_data = librosa.effects.time_stretch(self.audio_data, rate=self.playback_speed)
        self.audio_data = librosa.effects.pitch_shift(self.audio_data, sr=self.sr, n_steps=self.pitch_shift)