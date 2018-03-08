from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(rs=22, en=23, d4=24, d5=25, d6=26, d7=27, cols=16, lines=2)
lcd.clear()

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Set up input pin
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Callback function to run in another thread when button pressed
def buttonPressed(channel):
    lcd.clear()
    global counter
    counter += 1
    lcd.message('Button Pressed\n{0}'.format(counter))

# add event listener on pin 16
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(16, GPIO.RISING, callback=buttonPressed, bouncetime=150)
counter = 0
try:
    while True:
        sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."
