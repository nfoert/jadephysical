
from time import sleep

	
# Now define the voice_to_text() function for all platforms
import speech_recognition as sr

speech = sr.Recognizer()
def jadesr():
    print("JadeSR: ")
    voice_input = ""
    with sr.Microphone() as source:

        speech.adjust_for_ambient_noise(source)
        print("SPEAK!")
        audio = speech.listen(source)

        try:
            print("Recognizing...")
            voice_input = speech.recognize_google(audio)

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input