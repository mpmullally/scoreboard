from Adafruit_CharLCD import Adafruit_CharLCD
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Raspberry Pi pin configuration:
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_red   = 2
lcd_green = 3
lcd_blue  = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)
lcd.clear()

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(5, GPIO.FALLING, callback=my_callback, bouncetime=300)

GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback2, bouncetime=300)

def my_callback(channel):
    lcd.clear()
    lcd.set_color(1.0, 0.0, 0.0)
    lcd.message('Button Pressed')

def my_callback2(channel):
    plcd.clear()
    lcd.set_color(0.0, 0.0, 1.0)
    lcd.message('Button Pressed')

try:
    print "Waiting for rising edge on port 24"
    GPIO.wait_for_edge(24, GPIO.RISING)
    print "Rising edge detected on port 24. Here endeth the third lesson."

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
