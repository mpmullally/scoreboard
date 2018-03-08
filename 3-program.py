import time
import Adafruit_CharLCD as LCD

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
lcd.message("Red: 10\nBlue: 10")

time.sleep(5)
lcd.clear()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Set up input pin
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Callback function to run in another thread when button pressed
def buttonPressed(channel):
    lcd.clear()
    global counter
    counter += 1
    lcd.message('Button Pressed\n{0}'.format(counter))

# add event listener on pin 26
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(26, GPIO.RISING, callback=buttonPressed, bouncetime=150)
counter = 0
try:
    while True:
        sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."
