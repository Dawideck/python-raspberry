from picamera import PiCamera
from time import sleep
import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
sensorPin = 21 #dla BOARD 40

GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

camera = PiCamera()
camera.resolution = (640, 480)
camera.preview_window = (0, 0, 640, 480)

counter = 0
counter = str(counter)

def detectMotion(event):
    if GPIO.input(sensorPin):
        localtime = time.asctime(time.localtime(time.time()))
        print("Ruch wykryty! "+ localtime)
                
        camera.capture(localtime+".jpg")
        print("Cyk!")


GPIO.add_event_detect(sensorPin, GPIO.RISING, callback=detectMotion, bouncetime=100) 


try:
    while True:
        sleep(1)
        
except KeyboardInterrupt:
    print("zakonczono klawiatura")
    GPIO.cleanup()
    
finally:                 
    GPIO.cleanup()
