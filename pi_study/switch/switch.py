
import RPi.GPIO as gpio
from time import sleep

BUTTON_PINS = {13: '1', 19: '2', 26: '3'}
LED_PINS = {'1' : 16, '2' : 20, '3' : 21}

password = '112'
input_sequence = []

gpio.setmode(gpio.BCM)

for pin in BUTTON_PINS:
    gpio.setup(pin, gpio.IN, pull_up_down = gpio.PUD_DOWN)

for pin in LED_PINS.values():
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.LOW)

def indicate_button(number):
    led_pin = LED_PINS[number]
    gpio.output(led_pin, gpio.HIGH)
    sleep(0.3)
    gpio.output(led_pin, gpio.LOW)

def success_sequence():
    for _ in range(3):
        for pin in LED_PINS.values():
            gpio.output(pin, gpio.HIGH)
            sleep(0.3)
            gpio.output(pin, gpio.LOW)
            sleep(0.1)

def fail_sequence():
    for _ in range(3):
        for pin in LED_PINS.values():
            gpio.output(pin, gpio.HIGH)
        sleep(0.3)
        for pin in LED_PINS.values():
            gpio.output(pin, gpio.LOW)
        sleep(0.3)

try:
    print("비밀번호 입력 : ")

    while True:
        for pin, number in BUTTON_PINS.items():
            if gpio.input(pin) == gpio.HIGH:
                print(f"버튼 {number} 입력")
                indicate_button(number)
                input_sequence.append(number)
                sleep(0.5)

                if len(input_sequence) == 3:
                    entered = ''.join(input_sequence)
                    if entered == password:
                        success_sequence()
                    else:
                        fail_sequence()
                    input_sequence = []

except KeyboardInterrupt:
    print("종료")
finally:
    gpio.cleanup()