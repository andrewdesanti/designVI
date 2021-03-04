from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.on()
    print("BLINK")
    sleep(1)
    led.off()
    sleep(1)
