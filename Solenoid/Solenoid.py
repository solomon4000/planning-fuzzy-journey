import board
import digitalio
import time

SolenoidPin = 4

solenoid = digitalio.DigitalInOut(board.D4)

solenoid.direction = digitalio.Direction.OUTPUT 

while True:

    solenoid.value = True
    time.sleep(1)
    solenoid.value = False
    time.sleep(1)
