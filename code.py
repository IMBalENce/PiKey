import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

gp0 = digitalio.DigitalInOut(board.GP0)
gp0.direction = digitalio.Direction.INPUT
gp0.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.GP28)
led.direction = digitalio.Direction.OUTPUT
led.value = False

keyboard = Keyboard(usb_hid.devices)

# blink the LED three times
for _ in range(3):
    # light up the LED
    led.value = True
    # wait 0.5 seconds
    time.sleep(0.5)
    # turn off the LED
    led.value = False
    # wait 0.5 seconds
    time.sleep(0.5)

while True:
    # block while button is not pressed
    while gp0.value:
        pass
    print("Button pushed!")

    # light up the LED
    led.value = not led.value

    # send Cmd+Shift+A
    keyboard.send(Keycode.ALT, Keycode.A)

    # wait 0.5 seconds
    time.sleep(0.5)

    # turn off the LED
    # led.value = False

    # wait for button to be released
    while not gp0.value:
        pass
    
    