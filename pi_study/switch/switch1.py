import RPi.GPIO as gpio
from time import sleep

swPin = 13

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

try:
    while True:
        print(gpio.input(swPin))
        if gpio.input(swPin) == gpio.HIGH:
            print("버튼을 눌렀습니다.")
        else:
            print("버튼을 누르지 않았습니다.")
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()

