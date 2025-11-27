#!/usr/bin/python3
import sys
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')
import RPi.GPIO as GPIO
import os
import time
from multiprocessing import Process

# pins (BCM)
powerPin = 3      # power button
resetPin = 2      # reset button
ledPin = 14       # LED
powerenPin = 4    # power enable

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(powerenPin, GPIO.OUT)

    GPIO.output(powerenPin, GPIO.HIGH)

def poweroff():
    while True:
        GPIO.wait_for_edge(powerPin, GPIO.FALLING)
        os.system("poweroff")

def ledBlink():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        GPIO.wait_for_edge(powerPin, GPIO.FALLING)
        while GPIO.input(powerPin) == GPIO.LOW:
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.2)

def reset():
    while True:
        GPIO.wait_for_edge(resetPin, GPIO.FALLING)
        os.system("reboot")

if __name__ == "__main__":
    init()

    p1 = Process(target=poweroff)
    p2 = Process(target=ledBlink)
    p3 = Process(target=reset)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    GPIO.cleanup()
