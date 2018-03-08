from Adafruit_CharLCD import Adafruit_CharLCD

# Raspberry Pi pin configuration:
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
lcd.clear()

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Set up input pin
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

bluecounter = 0
redcounter = 0
# Callback function to run in another thread when button pressed
def RedPlus(channel):
    lcd.clear()
    global redcounter
    global bluecounter
    if redcounter <21:
        redcounter += 1
        lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
    else:
        lcd.message('RED WINS!!!')
        lcd.clear()
        lcd.message('New Game!!!')
        sleep(2)
        lcd.clear()
        redcounter = 0
        bluecounter = 0
        lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
# Callback function to run in another thread when button pressed
def RedReset(channel):
    lcd.clear()
    global redcounter
    global bluecounter
    redcounter = 11
    lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
# Callback function to run in another thread when button pressed
def BluePlus(channel):
    lcd.clear()
    global redcounter
    global bluecounter
    if bluecounter <21:
        redcounter += 1
        lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
    else:
        lcd.message('BLUE WINS!!!')
        lcd.clear()
        lcd.message('New Game!!!')
        sleep(2)
        lcd.clear()
        redcounter = 0
        bluecounter = 0
        lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
# Callback function to run in another thread when button pressed
def BlueReset(channel):
    lcd.clear()
    global redcounter
    global bluecounter
    counter = 11
    lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )
# Callback function to run in another thread when button pressed
# def Reset(channel):
     #lcd.clear()
     #lcd.message('New Game!!!')
     #sleep(2)
     #lcd.clear()
     #global redcounter == 0
     #global bluecounter == 0
     #lcd.message('Red: {0}'.format(redcounter)'\n Blue: {0}'.format(bluecounter) )

# add event listener on pin 26
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(26, GPIO.FALLING, callback=RedPlus, bouncetime=150)
# add event listener on pin 19
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(19, GPIO.FALLING, callback=RedReset, bouncetime=150)
# add event listener on pin 13
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(13, GPIO.FALLING, callback=BluePlus, bouncetime=150)
# add event listener on pin 6
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(6, GPIO.FALLING, callback=BlueReset, bouncetime=150)
# add event listener on pin 5
# event will interrupt the program and call the buttonPressed function
#GPIO.add_event_detect(5, GPIO.FALLING, callback=Reset, bouncetime=150)

try:
    while True:
        sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."
