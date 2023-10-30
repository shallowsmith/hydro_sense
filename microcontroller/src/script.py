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
    
    #temperature conversion from celsius to fahrenheit
    fahrenheit_temperature = (temperature * 9/5) + 32
    print(f"{fahrenheit_temperature} Degrees Fahrenheit")
    
    print("Humidity:", humidity, "%")

    # Send data to Firebase in JSON format
    ref = db.reference('sensor_data')
    ref.push({
        'temperature': temperature,
        'humidity': humidity,
        'time': time.time()
    })

    #Display time in format "2023-10-27 10:51:53"
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"{current_time}")
    
    time.sleep(30)
