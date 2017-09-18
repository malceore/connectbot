from time import sleep
from random import randint
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def stop():
    GPIO.output(25, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    print("stop")

def set_speed(test):
    print("speed")

def fwd():
    stop()
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    print("fwd")

def bwd():
    stop()
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    print("bwd")

def us_dist(test):
    print("us_dist")
    return randint(1,100)

def volt():
    print("volt")

def left_rot():
    stop()
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    print("left_rot")
    sleep(0.25)
    #stop()

def right_rot():
    stop()
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    print("right_rot")
    sleep(0.25)
    #stop()

stop()
