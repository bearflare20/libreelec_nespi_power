#!/usr/bin/python3
import os
import time
from multiprocessing import Process

# GPIO pin numbers (BCM)
powerPin = 3
resetPin = 2
ledPin = 14
powerenPin = 4

def export(pin):
    if not os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/export", "w") as f:
            f.write(str(pin))

def set_dir(pin, direction):
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def write(pin, value):
    with open(f"/sys/class/gpio/gpio{pin}/value", "w") as f:
        f.write(str(value))

def read(pin):
    with open(f"/sys/class/gpio/gpio{pin}/value", "r") as f:
        return f.read().strip()

def wait_for_falling(pin):
    # basic polling since sysfs doesnt support edge waits reliably everywhere
    while True:
        if read(pin) == "0":
            time.sleep(0.05)
            if read(pin) == "0":
                return
        time.sleep(0.05)

def init():
    export(powerPin)
    export(resetPin)
    export(ledPin)
    export(powerenPin)

    set_dir(powerPin, "in")
    set_dir(resetPin, "in")
    set_dir(ledPin, "out")
    set_dir(powerenPin, "out")

    write(powerenPin, 1)

def poweroff():
    while True:
        wait_for_falling(powerPin)
        os.system("poweroff")

def ledBlink():
    while True:
        write(ledPin, 1)
        wait_for_falling(powerPin)
        while read(powerPin) == "0":
            write(ledPin, 0)
            time.sleep(0.2)
            write(ledPin, 1)
            time.sleep(0.2)

def reset():
    while True:
        wait_for_falling(resetPin)
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
