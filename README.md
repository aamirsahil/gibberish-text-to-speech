# Gibberish Text to Speech

This project transforms plain text into **gibberish voice sounds** using a predefined dataset of audio clips mapped to characters and expressions. My motivation was primrily to produce voice system seen in games like Okami, Animal Crossing ect.

## What it does

Give it any text and it will:

- Break the text into characters.
- Match each character to a **pre-recorded gibberish sound** stored as `.wav` file.
- Identify special expressions like *laugh*, *angry*, etc., and attach fitting sounds.
- **Pitch-shift** and **speed up** the audio clips to create varied and dynamic speech-like output.
- Stitch it all together into one seamless gibberish audio file.

## How it works

1. Each character (like `a`, `b`, `c`...) has an associated gibberish sound.
2. The text is parsed one character at a time.
3. If expressions (like `[laugh]` or `[angry]`) are found, special sounds are inserted.
4. Each sound is pitch-shifted and sped up randomly for variation.
5. The processed clips are concatenated into a final audio output.

## Expression Support

The following expressions are supported and have their own dedicated sound effects:

- `[laugh]` — inserts a giggly or goofy sound
- `[angry]` — grumbly, aggressive gibberish
- `[happy]` — cheerful and bouncy tones
- `[sad]` — slower and gloomier gibberish
- `[confused]` — quirky or questioning intonations
- `[excited]` — fast, high-pitched gibberish

## File Structure

```
📁 repo/
├── 📁 src 
    ├── 📁 assets           # Audio file location
    ├── 📁 audio_modifier   # class to add audio effects to sound
    ├── 📁 gibberish_tts    # Gibberish generator class
    ├── 📁 pytts            # Pyttsx3 class
    ├── 📁 text_to_speech   # Ochestration class
    ├── 📁 models           # dataclass model
    ├── data.json        # Text data
    ├── generate.py      # Generate funciton
├── 📁 test                 
├── 📁 env                  
├── README.md            
```

## Requirements

- Python 3.x

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python generate.py
```
This will play the corresponding gibberish audio. The text to play should be in src/data.json file.

## Customize

To add your own sounds Just update `src\assets\sound_files\alphabets` with your audio clips. You can also tweak pitch and speed settings inside `generate.py`.