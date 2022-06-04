#| Jade Physical Edition
#| Version BETA 5
#| 9-7-21
#|--
# Under no circmstances may you copy, paste, change, or modify parts of this code, and
# all refrenced modules unless you have written permission from the creator.
#| (c) Noah Foertmeyer
#|--
# Many pieces of Jade Physical Edition was taken from the online repoitory for the book
# 'Make Python Talk' by Mark Liu, then adjusted to fit my needs.
#|--



# -----
# Preparation
# -----

# Imports
from jadesr import jadesr # Custom module for handling speech recognition.
from jadesay import jadesay # Custom module for handling text-to-speech.
from mywakeup import wakeup # Custom module for handling standby mode.
from time import sleep # time.sleep is a wait function
import os # os module
# Custom module for handling LED animations
import ezgmail
import arrow

global prev
prev = None
# -----
# Main Code
# -----

while True:
    # Capture your voice command quietly in standby
    wake_up = wakeup()
    # You can wake up the VPA by saying "Hello Python"
    while wake_up == "Activated":
        if prev != " " or "":
            os.system("aplay noise.wav")
        
        inp = jadesr().lower()
        #jadesay(f'You just said {inp}.')
        print(f"You just said: {inp}")

        # Conditional chain for formulating a response.
        if "standby" in inp:
            jadesay("Entering standby mode.")
            break
        
        elif "" or " " in inp:
            prev = inp
            break

        elif "hello" in inp:
            jadesay("Hello, there!")

        elif "how are you" in inp:
            jadesay("I don't have feelings.")

        elif "shutdown" in inp or "shut" and "down" in inp:
            jadesay("Are you sure you want me to shut down?")

            while True:
                shdw = jadesr().lower()
                jadesay(f'You just said {shdw}.')
                if "yes" in shdw:
                    jadesay("Alright. I'll shut down.")

                    #os.system("sudo shutdown now")
                    print("SHUT DOWN")

                elif "no" in shdw:
                    jadesay("Okay. I won't shut down.")
                    break

                elif " " in shdw or "" in shdw:
                    jadesay("I didn't get that. Please try again.")

                else:
                    jadesay("That's not a yes or a no.")


        elif "restart" in inp or "reboot" in inp:
            jadesay("Are you sure you want me to restart?")

            while True:
                res = jadesr().lower()
                jadesay(f'You just said {res}.')
                if "yes" in res:
                    jadesay("Alright. I'll restart.")


                    #os.system("sudo reboot")
                    print("RESTART")

                elif "no" in res:
                    jadesay("Okay. I won't shut down.")
                    break

                elif " " in res or "" in res:
                    jadesay("I didn't get that. Please try again.")

                else:
                    jadesay("That's not a yes or a no.")

        elif "read" and "email" in inp or "unread" and "email" in inp:
                jadesay("Getting unread emails from nofoert@gmail.com")
                unreadThreads = ezgmail.unread()
                ezgmail.summary(unreadThreads)
                jadesay(str(ezgmail.summary(unreadThreads)))


        elif "send" and "email" in inp:

            while True:
                jadesay("Who do you want to send the email to?")
                recipentInp = jadesr().lower()
                sleep(1)
                jadesay(f'You just said {recipentInp}.')
                if "mom" in recipentInp or "erin" in recipentInp:
                    jadesay("I'll send the email to efo_08@hotmail.com")
                    recipent = "efo_08@hotmail.com"
                    break
                elif "dad" in recipentInp or "matt" in recipentInp:
                    jadesay("I'll send the email to mattfoertmeyer@yahoo.com")
                    recipent = "mattfoertmeyer@yahoo.com"
                    break
                elif "noah" in recipentInp or "me" in recipentInp:
                    jadesay("I'll send the email to nofoert@gmail.com")
                    recipent = "nofoert@gmail.com"
                    break
                elif "charlotte" in recipentInp or "sister" in recipentInp:
                    jadesay("I'll send the email to chafoert@gmail.com")
                    recipent = "chafoert@gmail.com"
                    break
                else:
                    jadesay("I didn't see that person in your contact list.")
                    continue

            sleep(1)

            jadesay("What do you want the subject line to be?")
            subLine = jadesr().lower()
            sleep(1)
            jadesay(f'You just said {subLine}.')

            sleep(1)

            jadesay("What do you want the body to be?")
            body = jadesr().lower()
            sleep(1)
            jadesay(f'You just said {body}.')
            sleep(1)
            ezgmail.send(recipent, subLine, body)
            jadesay("Okay. I sent the email.")

        elif "time" and "is" and "it" in inp:
            currentTime = arrow.now().format("H:m A")
            jadesay("It's " + currentTime)

        elif "who" and "you" in inp:
            jadesay("I'm Jade, but I thought you already knew that.")



        else:
            if "" in inp or " " in inp:
                prev = " "
                continue
            elif "" != inp or " " != inp:
                jadesay("I didn't get that.")
                continue
            else:
                jadesay("I didn't get that.")
                continue

    if wake_up == "ToQuit":
        jadesay("Okay. I'll quit.")
        break