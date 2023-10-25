import RPi.GPIO as GPIO

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 3  # Input PIN unknown for now
GPIO.setup(SENSOR_PIN, GPIO.IN)

value = GPIO.input(SENSOR_PIN)

print(GPIO.input(value))

GPIO.cleanup()
