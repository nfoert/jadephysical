import os

def jadesay(input):
    print("JadeSay: ")
    print(input)
    os.system('gtts-cli --nocheck "' + input + '" | mpg123 -q -')