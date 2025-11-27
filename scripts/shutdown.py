#!/usr/bin/python3
import sys
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')

from gpiozero import DigitalInputDevice LED
import os
import time
from multiprocessing import Process

powerPin = 3
resetPin = 2
ledPin = 14
powerenPin = 4

power = DigitalInputDevice(powerPin pull_up=True)
reset = DigitalInputDevice(resetPin pull_up=True)
led = LED(ledPin)
powerenable = LED(powerenPin)
powerenable.on()

def poweroff():
    while True:
        if power.value == 0:
            os.system("poweroff")
        time.sleep(0.1)

def resetfunc():
    while True:
        if reset.value == 0:
            os.system("reboot")
        time.sleep(0.1)

def ledblink():
    while True:
        led.on()
        if power.value == 0:
            while power.value == 0:
                led.off()
                time.sleep(0.2)
                led.on()
                time.sleep(0.2)
        time.sleep(0.1)

if __name__ == "__main__":
    from multiprocessing import Process
    p1 = Process(target=poweroff)
    p2 = Process(target=resetfunc)
    p3 = Process(target=ledblink)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
