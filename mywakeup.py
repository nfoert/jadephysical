from gpiozero import PWMLED
from time import sleep
import defLED
from LEDfunc import LEDfadeIn, LEDfadeOut, LEDpairFadeIn, LEDpairFadeOut


# Now define the wakeup() function for all platforms
import speech_recognition as sr

speech = sr.Recognizer()
# define a wakeup() function to determine the status of the VPA
def wakeup():
    wakeup = "StandBy"	
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            LEDpairFadeIn(defLED.LEDgreen1, defLED.LEDgreen2)
            print("Say 'hello' to activate Jade.")
            defLED.LEDgreen1.off()
            defLED.LEDgreen2.off()
            sleep(0.25)
            defLED.LEDgreen1.on()
            defLED.LEDgreen2.on()
            audio = speech.listen(source,timeout=3)
            LEDpairFadeOut(defLED.LEDgreen1, defLED.LEDgreen2)
            print("Recognizing...")
            voice_input = speech.recognize_google(audio).lower()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    if "hello" in voice_input or "asststant" in voice_input or "hey" in voice_input or "jade" in voice_input:
        wakeup = "Activated"
    elif "stop" in voice_input or "quit" in voice_input or "shut" and "down" in voice_input:
        wakeup = "ToQuit"
    return wakeup

    LEDred1.close()
    LEDred2.close()
    LEDgreen1.close()
    LEDgreen2.close()