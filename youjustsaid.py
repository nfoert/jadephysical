from jadesay import jadesay
from time import sleep
def youjustsaid(inp):
    print("YouJustSaid: ")
    if inp == "" or inp == " ":
        jadesay("I didn't get that.")
    else:
        jadesay("You just said: ")
        sleep(0.25)
        jadesay(inp)