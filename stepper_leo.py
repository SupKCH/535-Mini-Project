## Originally created by Leo
## Edited by SupKCH

from gpiozero import LED
from time import sleep

def sleep_func(continuous, sl_time):
    if not continuous:
        sleep(sl_time)
    else:
        pass

class stepper():
    def __init__(self, pulse_pin, direction_pin, enable_pin, delay=0.0005, sleep_time=0.25):
        self.PUL = LED(pulse_pin)
        self.DIR = LED(direction_pin)
        self.ENA = LED(enable_pin)
        self.delay = delay
        self.sleep_time = sleep_time
    
    def forward(self, step=1, continuous=False):
        self.ENA.on()
        sleep_func(continuous, self.sleep_time)
        self.DIR.off()
        self.PUL.blink(self.delay, self.delay, step)
        sleep_func(continuous, self.sleep_time)
        return

    def backward(self, step=1, continuous=False):
        self.ENA.on()
        sleep_func(continuous, self.sleep_time)
        self.DIR.on()
        self.PUL.blink(self.delay, self.delay, step)
        sleep_func(continuous, self.sleep_time)
        return

    def stop(self):
        self.ENA.off()
        self.PUL.off()
