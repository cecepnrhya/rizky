import RPi.GPIO as GPIO
import time


class ServoControl:
    def __init__(self):
        self.servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(self.servoPIN, 50)  # GPIO 17 for PWM with 50Hz

    def move_servo(self):
        self.p.start(2.5)  # Initialization
        try:

            self.p.ChangeDutyCycle(5)
            time.sleep(4)
            self.p.ChangeDutyCycle(10)
            time.sleep(4)
        except KeyboardInterrupt:
            self.p.stop()
            GPIO.cleanup()