import RPi.GPIO as GPIO
import time
#import sys 

out1 = 11
out2 = 12
out3 = 15
out4 = 16

enA = 29
enB = 31

i=0
positive=0
negative=0
y=0
delayTime = 0.1


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(enA,GPIO.HIGH)
GPIO.output(enB,GPIO.HIGH)

GPIO.output(out1,GPIO.HIGH)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
time.sleep(2)
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.HIGH)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
time.sleep(2)
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.HIGH)
GPIO.output(out4,GPIO.LOW)
time.sleep(2)
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.HIGH)
time.sleep(2)

GPIO.cleanup()