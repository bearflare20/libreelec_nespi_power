#!/usr/bin/python3
import sys
import RPi.GPIO as GPIO
import os
import time
from multiprocessing import Process

# initialize pins
powerPin = 3      # pin 5 (power button)
ledPin = 14       # TXD
resetPin = 2      # pin 13 (reset button)
powerenPin = 4    # pin 5 (power enable)

# GPIO initialization
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(powerenPin, GPIO.OUT)
    GPIO.output(powerenPin, GPIO.HIGH)
    GPIO.setwarnings(False)

# Poweroff handler (LibreELEC uses busybox poweroff)
def poweroff():
    while True:
        GPIO.wait_for_edge(powerPin, GPIO.FALLING)
        os.system("poweroff")

# LED blink during power button hold
def ledBlink():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        GPIO.wait_for_edge(powerPin, GPIO.FALLING)
        while GPIO.input(powerPin) == GPIO.LOW:
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.2)

# Reset handler (LibreELEC reboot command)
def reset():
    while True:
        GPIO.wait_for_edge(resetPin, GPIO.FALLING)
        os.system("reboot")

if __name__ == "__main__":
    init()

    powerProcess = Process(target=poweroff)
    ledProcess = Process(target=ledBlink)
    resetProcess = Process(target=reset)

    powerProcess.start()
    ledProcess.start()
    resetProcess.start()

    powerProcess.join()
    ledProcess.join()
    resetProcess.join()

    GPIO.cleanup()
