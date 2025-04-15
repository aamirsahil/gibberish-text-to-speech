from text_to_speech import TextToSpeechV1
import json
import os

def main():
    text_to_speech = TextToSpeechV1()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'data.json')
    
    with open(data_path, 'r') as f:
        data = json.load(f)
        text = data['content'][0]['text']

    text_to_speech.load_speech(text)
    text_to_speech.play_speech()

if __name__=="__main__":
    main()