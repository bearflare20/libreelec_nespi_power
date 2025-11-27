#!/usr/bin/python3
from gpiozero import Button, LED
import os
import time
from multiprocessing import Process

# BCM pins
powerPin = 3
resetPin = 2
ledPin = 14
powerenPin = 4

# objects
powerBtn = Button(powerPin, pull_up=True, bounce_time=0.05)
resetBtn = Button(resetPin, pull_up=True, bounce_time=0.05)
led = LED(ledPin)
powerEnable = LED(powerenPin)
powerEnable.on()

def poweroff():
    while True:
        powerBtn.wait_for_press()
        os.system("poweroff")

def ledBlink():
    while True:
        led.on()
        powerBtn.wait_for_press()
        while powerBtn.is_pressed:
            led.off()
            time.sleep(0.2)
            led.on()
            time.sleep(0.2)

def reset():
    while True:
        resetBtn.wait_for_press()
        os.system("reboot")

if __name__ == "__main__":
    p1 = Process(target=poweroff)
    p2 = Process(target=ledBlink)
    p3 = Process(target=reset)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
