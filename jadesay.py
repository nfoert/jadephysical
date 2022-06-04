import os
def jadesay(input):
    print(f"JadeSay: {input}")
    print(input)
    os.system(f'espeak -v male2 "{input}"')