from time import sleep
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(25, GPIO.LOW)
GPIO.output(25, GPIO.HIGH)
sleep(0.1)
GPIO.output(25, GPIO.LOW)
sleep(0.5)

GPIO.output(24, GPIO.LOW)
GPIO.output(24, GPIO.HIGH)
sleep(0.1)
GPIO.output(24, GPIO.LOW)
sleep(0.5)

GPIO.output(23, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)
sleep(0.1)
GPIO.output(23, GPIO.LOW)
sleep(0.5)

GPIO.output(18, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)
sleep(0.1)
GPIO.output(18, GPIO.LOW)
sleep(0.5)


