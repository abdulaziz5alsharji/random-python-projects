try:
    import playsound
    import speech_recognition as speech
    from gtts import gTTS
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Enter to exit")
    sys.exit()


# Function compile text to audio
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = f"voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


# Function compile audio to text
def get_audio():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as error:
            print(error)
    return said


text = get_audio()
if "hello" in text:
    speak("hello how are you")
elif "i am fine" in text:
    speak("that is good")
elif "how are you" in text:
    speak("i am fine what about you")
elif "what is your name" in text:
    speak("my name is sarah")
elif "what are you doing" in text:
    speak("i am writing coding new what about you")
elif "where are you from" in text:
    speak("you make me so do not ask me this question")
else:
    speak("i do not understand you")
