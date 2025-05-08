import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 20, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)
    
try:
    isOnAll = False
    while True:
        for pin in ledPin:
            for i in range(2):
                gpio.output(pin, gpio.HIGH)
                sleep(0.5)
                gpio.output(pin, gpio.LOW)
                sleep(0.5)

        
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()
    
