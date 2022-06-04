from time import sleep

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
            print("Standby: Say 'Hey Jade' to activate Jade.")
            audio = speech.listen(source,timeout=3)

            print("Standby: Recognizing...")
            voice_input = speech.recognize_google(audio).lower()
            print("Standby: Done.")
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    if "hey" in voice_input and "jade" in voice_input or "hello" in voice_input:
        wakeup = "Activated"
        print("Standby: Now activated.")
    
    elif "stop" in voice_input or "quit" in voice_input or "shut" and "down" in voice_input:
        wakeup = "ToQuit"
    return wakeup

    LEDred1.close()
    LEDred2.close()
    LEDgreen1.close()
    LEDgreen2.close()