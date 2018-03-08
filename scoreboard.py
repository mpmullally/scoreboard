RedScore = 0
BlueScore = 0

from time import sleep
while RedScore <= 5 and BlueScore <= 5:
    if RedScore == 5:
        print('RED WINS')
        sleep(2)
        RedScore = BlueScore = 0
        continue
    elif BlueScore == 5:
        print('BLUE WINS')
        sleep(2)
        BlueScore = RedScore = 0
        continue
    else:
        x = input("Who Scored? ")
        if x == 'Red':
            RedScore += 1
            print(RedScore)
        elif x == 'Blue':
            BlueScore += 1
            print(BlueScore)
        elif x == 'REDRESET':
            RedScore = 3
            print(RedScore)
        elif x == 'BLUERESET':
            BlueScore = 3
            print(BlueScorecore)
        else:
            print('Bad Input')


#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#while True:
#input_state = GPIO.input(18)
#if input_state == False:
#RedScore += 1
#time.sleep(0.2)
