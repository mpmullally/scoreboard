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

RedScore = 0
BlueScore = 0

from time import sleep
while RedScore <= 5 and BlueScore <= 5:
    if RedScore == 5:
        lcd.clear()
        lcd.message('RED WINS!!!')
        sleep(2)
        RedScore = BlueScore = 0
        continue
    elif BlueScore == 5:
        lcd.clear()
        lcd.message('BLUE WINS!!!')
        sleep(2)
        BlueScore = RedScore = 0
        continue
    else:
        x = input("Who Scored? ")
        if x == 'Red':
            RedScore += 1
            lcd.clear()
            lcd.message('Red: 'RedScore'  Blue:'BlueScore)
        elif x == 'Blue':
            BlueScore += 1
            lcd.clear()
            lcd.message('Red: 'RedScore'  Blue:'BlueScore)
        elif x == 'REDRESET':
            RedScore = 3
            lcd.clear()
            lcd.message('Red: 'RedScore'  Blue:'BlueScore)
        elif x == 'BLUERESET':
            BlueScore = 3
            lcd.clear()
            lcd.message('Red: 'RedScore'  Blue:'BlueScore)
        else:
            lcd.clear()
            lcd.message('Bad Input')
