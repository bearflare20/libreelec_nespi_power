import sys
import os
import time
from multiprocessing import Process

# add the virtual rpi-tools lib path
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')

import lgpio

# pins
powerPin = 3
ledPin = 14
resetPin = 2
powerenPin = 4

# initialize GPIO
def init():
    global chip
    chip = lgpio.gpiochip_open(0)  # open gpio chip 0
    # inputs
    lgpio.gpio_claim_input(chip, powerPin)
    lgpio.gpio_claim_input(chip, resetPin)
    # outputs
    lgpio.gpio_claim_output(chip, ledPin, 0)
    lgpio.gpio_claim_output(chip, powerenPin, 1)  # HIGH
    print("GPIO initialized 🔥")

# wait for button and power off
def poweroff():
    while True:
        while lgpio.gpio_read(chip, powerPin):
            time.sleep(0.1)
        os.system("kodi-send --action=Powerdown")
        time.sleep(5)
        os.system("shutdown --poweroff now")

# blink LED when button held
def ledBlink():
    while True:
        while lgpio.gpio_read(chip, powerPin):
            time.sleep(0.1)
        start = time.time()
        while lgpio.gpio_read(chip, powerPin) == 0:
            lgpio.gpio_write(chip, ledPin, 0)
            time.sleep(0.2)
            lgpio.gpio_write(chip, ledPin, 1)
            time.sleep(0.2)

# reset pi
def reset():
    while True:
        while lgpio.gpio_read(chip, resetPin):
            time.sleep(0.1)
        os.system("shutdown -r now")

if __name__ == "__main__":
    init()
    powerProcess = Process(target=poweroff)
    powerProcess.start()
    ledProcess = Process(target=ledBlink)
    ledProcess.start()
    resetProcess = Process(target=reset)
    resetProcess.start()

    powerProcess.join()
    ledProcess.join()
    resetProcess.join()

    lgpio.gpiochip_close(chip)
