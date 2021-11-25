import defLED
from LEDfunc import LEDfadeIn, LEDfadeOut, LEDpairFadeIn, LEDpairFadeOut
from time import sleep

	
# Now define the voice_to_text() function for all platforms
import speech_recognition as sr

speech = sr.Recognizer()
def jadesr():
    print("JadeSR: ")
    voice_input = ""
    with sr.Microphone() as source:

        speech.adjust_for_ambient_noise(source)

        try:
            LEDpairFadeIn(defLED.LEDgreen1, defLED.LEDgreen2)
            defLED.LEDgreen1.off()
            defLED.LEDgreen2.off()
            sleep(0.25)
            defLED.LEDgreen1.on()
            defLED.LEDgreen2.on()
            audio = speech.listen(source)
            defLED.LEDgreen1.on()
            defLED.LEDgreen2.on()
            print("Recognizing...")
            voice_input = speech.recognize_google(audio)

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input