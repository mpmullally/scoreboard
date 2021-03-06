import RPi.GPIO as GPIO
import time
from time import sleep
import Adafruit_CharLCD as LCD

# Raspberry Pi configuration:
lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_red   = 4
lcd_green = 17
lcd_blue  = 7  # Pin 7 is CE1

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)
lcd.clear()
lcd.set_color(0.0,0.0,0.0)

GPIO.setmode(GPIO.BCM)

bluebutton = 5
blueresetbutton = 6
resetbutton = 13
redresetbutton = 19
redbutton = 26

global BlueScore
global RedScore

GPIO.setup(bluebutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(blueresetbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(resetbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redresetbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def bluebutton(channel):
    global BlueScore
    BlueScore = BlueScore + 1
    lcd.clear()
    lcd.set_color(0.0, 0.0, 1.0)
    lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
    sleep(2)

def blueresetbutton(channel):
    global BlueScore
    BlueScore = 11
    lcd.clear()
    lcd.set_color(0.0, 0.0, 1.0)
    lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
    sleep(2)

def resetbutton(channel):
    global RedScore
    global BlueScore
    RedScore = BlueScore = 0
    lcd.clear()
    lcd.set_color(1.0, 1.0, 0.0)
    lcd.message('NEW GAME!!!\nRed: '+str(RedScore)+'  Blue:'+str(BlueScore))
    sleep(2)

def redresetbutton(channel):
    global RedScore
    RedScore = 11
    lcd.clear()
    lcd.set_color(1.0, 0.0, 0.0)
    lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
    sleep(2)

def redbutton(channel):
    global RedScore
    RedScore = Redscore + 1
    lcd.clear()
    lcd.set_color(1.0, 0.0, 0.0)
    lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
    sleep(2)

    
GPIO.add_event_detect(5, GPIO.FALLING, callback=bluebutton, bouncetime=300)
GPIO.add_event_detect(6, GPIO.FALLING, callback=blueresetbutton, bouncetime=300)
GPIO.add_event_detect(13, GPIO.FALLING, callback=resetbutton, bouncetime=300)
GPIO.add_event_detect(19, GPIO.FALLING, callback=redresetbutton, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=redbutton, bouncetime=300)

RedScore = 0
BlueScore = 0
while RedScore <= 21 and BlueScore <= 21:
    if RedScore == 21:
        lcd.clear()
        lcd.set_color(1.0, 0.0, 0.0)
        lcd.message('RED WINS!!!')
        sleep(2)
        RedScore = BlueScore = 0
        lcd.clear()
        lcd.set_color(1.0, 1.0, 0.0)
        lcd.message('NEW GAME!!!\nRed: '+str(RedScore)+'  Blue:'+str(BlueScore))
        sleep(2)
        continue
    elif BlueScore == 21:
        lcd.clear()
        lcd.set_color(0.0, 0.0, 1.0)
        lcd.message('BLUE WINS!!!')
        sleep(2)
        BlueScore = RedScore = 0
        lcd.clear()
        lcd.set_color(1.0, 1.0, 0.0)
        lcd.message('NEW GAME!!!\nRed: '+str(RedScore)+'  Blue:'+str(BlueScore))
        sleep(2)
        continue
    else:
        lcd.clear()
        lcd.set_color(1.0, 1.0, 0.0)
        lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
        sleep(1)
