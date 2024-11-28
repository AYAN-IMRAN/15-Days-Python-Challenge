import pyttsx3

engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Set the voice to a female voice (you can choose a different voice by changing the index)
for voice in voices:
    if 'Female' in str(voice):
        engine.setProperty('voice', voice.id)
        break

# Set the language to Urdu (you can choose a different language by changing the code)
engine.setProperty('language', 'ur')

# Set the text to speak
text = "hello world"

# Speak the text
engine.say(text)
engine.runAndWait()