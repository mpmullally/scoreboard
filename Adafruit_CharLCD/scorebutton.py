from Adafruit_CharLCD import Adafruit_CharLCD
#37, 35, 33, 31, 29, 23
lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)
lcd.clear()

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

#26, 24, 22, 18, 16
# Set up input pin
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global bluecounter = 0
global redcounter = 0
# Callback function to run in another thread when button pressed
def RedPlus(channel):
    lcd.clear()
    global redcounter
    if redcounter <21:
        redcounter += 1
        lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
    else:
        lcd.message('RED WINS!!!')
# Callback function to run in another thread when button pressed
def RedReset(channel):
    lcd.clear()
    global redcounter
    redcounter = 11
    lcd.message('Red: {0}'.format(redcounter))
# Callback function to run in another thread when button pressed
def BluePlus(channel):
    lcd.clear()
    global bluecounter
    if bluecounter <21:
        redcounter += 1
        lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
    else:
        lcd.message('BLUE WINS!!!')
# Callback function to run in another thread when button pressed
def BlueReset(channel):
    lcd.clear()
    global bluecounter
    counter = 11
    lcd.message('Button Pressed\n{0}'.format(counter))
# Callback function to run in another thread when button pressed
def Reset(channel):
    lcd.clear()
    lcd.message('New Game!!!')
    sleep(2)
    lcd.clear()
    lcd.message('Red: 0 \nBlue: 0')

# add event listener on pin 16
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(16, GPIO.RISING, callback=RedPlus, bouncetime=150)
counter = 0
# add event listener on pin 17
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(17, GPIO.RISING, callback=RedReset, bouncetime=150)
counter = 0
# add event listener on pin 18
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(18, GPIO.RISING, callback=BluePlus, bouncetime=150)
counter = 0
# add event listener on pin 19
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(19, GPIO.RISING, callback=BlueReset, bouncetime=150)
counter = 0
# add event listener on pin 20
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(20, GPIO.RISING, callback=Reset, bouncetime=150)
counter = 0

try:
    while True:
        sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."
