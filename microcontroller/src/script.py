import board
import busio
import adafruit_sht31d
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('key.json') 
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hydro-sense-default-rtdb.firebaseio.com/' 
})

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

while True:
    temperature = round(sensor.temperature, 2)
    humidity = round(sensor.relative_humidity, 2)

    print("Temperature:", temperature, " Celsius")
    print("Humidity:", humidity, "%")

    # Send data to Firebase
    ref = db.reference('sensor_data')
    ref.push({
        'temperature': temperature,
        'humidity': humidity,
        'time': time.time()
    })


    time.sleep(30)


# Celsius to Fahrenheit function (Not used yet)
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
