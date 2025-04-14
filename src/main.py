from text_to_speech import TextToSpeechV1

def main():
    text_to_speech = TextToSpeechV1()
    text = "hi"
    text_to_speech.load_speech(text)
    text_to_speech.play_speech()

if __name__=="__main__":
    main()