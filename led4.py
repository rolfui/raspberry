from gpiozero import LED

RED = LED(25)
BUTTON = Button(8)

while True:
    if BUTTON.is_pressed:
        RED.on()
    else:
        RED.off()

#https://www.raspberrypi.org/documentation/usage/gpio/python/README.md
