import board # initiates board
import digitalio # allows communication with board output
import time # allows for breaks between actions

solenoid = digitalio.DigitalInOut(board.D4) # pin that goes to solenoid is 4

solenoid.direction = digitalio.Direction.OUTPUT # solenoid is used as output

while True:

    solenoid.value = True # set as true
    time.sleep(1) # stop 1
    solenoid.value = False # switch off solenoid
    time.sleep(1)
