import RPi.GPIO as GPIOimport
import time
GPIO.setmode(GPIO.BOARD)
TRIG = 13
ECHO = 15
green=18
yellow=7
red=11
i=0
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
print ("Calibrating.....")
time.sleep(2)
print ("Calculating Vehicle Distance......")
try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
           pulse_start = time.time()
        while GPIO.input(ECHO)==1:
           pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance+1.15, 2)
        if distance<=20 and distance>=5:
            print ("distance:",distance,"cm")
            GPIO.output(yellow, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(yellow, GPIO.LOW)
            GPIO.output(green, GPIO.HIGH)
            time.sleep(30)
            GPIO.output(green, GPIO.LOW)
            i=1
        if distance>20 and i==1:
            GPIO.output(yellow, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(yellow, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
            time.sleep(60)
            GPIO.output(red, GPIO.LOW)
            i=0
except KeyboardInterrupt:
    GPIO.cleanup()
    
    