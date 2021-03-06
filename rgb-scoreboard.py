#!/usr/bin/python
# Example using an RGB character LCD wired directly to Raspberry Pi or BeagleBone Black.
import time

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

RedScore = 0
BlueScore = 0

from time import sleep
while RedScore <= 5 and BlueScore <= 5:
    if RedScore == 5:
        lcd.clear()
        lcd.set_color(1.0, 0.0, 0.0)
        lcd.message('RED WINS!!!')
        sleep(2)
        RedScore = BlueScore = 0
        continue
    elif BlueScore == 5:
        lcd.clear()
        lcd.set_color(0.0, 0.0, 1.0)
        lcd.message('BLUE WINS!!!')
        sleep(2)
        BlueScore = RedScore = 0
        continue
    else:
        lcd.set_color(1.0, 1.0, 0.0)
        x = raw_input("Who Scored? ")
        if x == 'Red':
            RedScore += 1
            lcd.clear()
            lcd.set_color(1.0, 0.0, 0.0)
            lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
        elif x == 'Blue':
            BlueScore += 1
            lcd.clear()
            lcd.set_color(0.0, 0.0, 1.0)
	    lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
        elif x == 'REDRESET':
            RedScore = 3
            lcd.clear()
            lcd.set_color(1.0, 1.0, 1.0)
            lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))        
        elif x == 'BLUERESET':
            BlueScore = 3
            lcd.clear()
            lcd.set_color(1.0, 1.0, 1.0)
            lcd.message('Red: '+str(RedScore)+'  Blue:'+str(BlueScore))
        else:
            lcd.clear()
            lcd.set_color(1.0, 1.0, 1.0)
            lcd.message('Bad Input')
            sleep(2)
