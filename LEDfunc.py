import defLED
from time import sleep

def LEDfadeIn(led):
    print("LEDfunc.LEDfadeIn")
    led.value = 0
    sleep(0.03)
    led.value = 0.1
    sleep(0.03)
    led.value = 0.2
    sleep(0.03)
    led.value = 0.3
    sleep(0.03)
    led.value = 0.4
    sleep(0.03)
    led.value = 0.5
    sleep(0.03)
    led.value = 0.6
    sleep(0.03)
    led.value = 0.7
    sleep(0.03)
    led.value = 0.8
    sleep(0.03)
    led.value = 0.9
    sleep(0.03)
    led.value = 1
    sleep(0.03)

def LEDfadeOut(led):
    print("LEDfunc.LEDfadeOut")
    led.value = 1
    sleep(0.03)
    led.value = 0.9
    sleep(0.03)
    led.value = 0.8
    sleep(0.03)
    led.value = 0.7
    sleep(0.03)
    led.value = 0.6
    sleep(0.03)
    led.value = 0.5
    sleep(0.03)
    led.value = 0.4
    sleep(0.03)
    led.value = 0.3
    sleep(0.03)
    led.value = 0.2
    sleep(0.03)
    led.value = 0.1
    sleep(0.03)
    led.value = 0
    sleep(0.03)

def LEDpairFadeIn(led1, led2):
    print("LEDfunc.LEDpairFadeIn")
    led1.value = 0.1
    led2.value = 0.1
    sleep(0.03)
    led1.value = 0.2
    led2.value = 0.2
    sleep(0.03)
    led1.value = 0.3
    led2.value = 0.3
    sleep(0.03)
    led1.value = 0.4
    led2.value = 0.4
    sleep(0.03)
    led1.value = 0.5
    led2.value = 0.5
    sleep(0.03)
    led1.value = 0.6
    led2.value = 0.6
    sleep(0.03)
    led1.value = 0.7
    led2.value = 0.7
    sleep(0.03)
    led1.value = 0.8
    led2.value = 0.8
    sleep(0.03)
    led1.value = 0.9
    led2.value = 0.9
    sleep(0.03)
    led1.value = 1
    led2.value = 1
    sleep(0.03)

def LEDpairFadeOut(led1, led2):
    print("LEDfunc.LEDpairFadeOut")
    led1.value = 1
    led2.value = 1
    sleep(0.03)
    led1.value = 0.9
    led2.value = 0.9
    sleep(0.03)
    led1.value = 0.8
    led2.value = 0.8
    sleep(0.03)
    led1.value = 0.7
    led2.value = 0.7
    sleep(0.03)
    led1.value = 0.6
    led2.value = 0.6
    sleep(0.03)
    led1.value = 0.5
    led2.value = 0.5
    sleep(0.03)
    led1.value = 0.4
    led2.value = 0.4
    sleep(0.03)
    led1.value = 0.3
    led2.value = 0.3
    sleep(0.03)
    led1.value = 0.2
    led2.value = 0.2
    sleep(0.03)
    led1.value = 0.1
    led2.value = 0.1
    sleep(0.03)
    led1.value = 0
    led2.value = 0
    sleep(0.03)