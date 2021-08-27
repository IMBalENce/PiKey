# PiKey
A customisable physical shortcut key based on Raspberry Pi Pico. I designed this to make it easier to mute/unmute microphone for my kids during home-schooling on Zoom, so that I don't have to keep alert for teacher's cue to unmute.

It's not the most cost-effecitive design, nor the smallest form factor that I can make. But it's all I have on hand during the 6th lock down in Melbourne. I need it for the class this weekend. I hope this can help the other parents with the same the headache.

## What you need:
(I purchased most of my parts from core-electronics but can be sourced from elsewhere)

- Raspberry pi Pico https://core-electronics.com.au/raspberry-pi-pico.html
- PiicoDev Expansion Board for Pico (not necessary but easier for mounting) https://core-electronics.com.au/piicodev-expansion-board-for-pico.html
- Four jumper wires
- small LED and current limiting resistor
- Momentary Push Button (12mm square one is used in this design)
- A case (I 3d printed mine and the stl files are attached)

## Installation:
- Assemble parts together according to the image.

![plot](./img/Assem%202.JPG)

- Push button is connected to GPIO0, LED with current limiting resistor is connected to GPIO28. (change to whichever suits and modify the code.py file)
- Install Circuitpython following the instruction below
  https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/installing-circuitpython
- Down the Circuitpython libraries from the link below
  https://circuitpython.org/libraries
- Copy the adafruit_hid folder from the library bundle to the lib folder on the CIRCUITPY drive.
- Copy code.py from this repo to the root directory on the CIRCUITPY drive

## Reference
https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/overview

https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3
