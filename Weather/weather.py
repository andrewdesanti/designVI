import geocoder, requests, json, time
import datetime as dt
import RPi.GPIO as GPIO

#gpio setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
rain = ["shower rain", "rain", "thunderstorm", "snow", "mist"]
#openweatherapi setup
key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
urlBase = "https://api.openweathermap.org/data/2.5/weather?"
#geocoder for coordiantes
location = geocoder.ip('me')
coord = location.latlng
lat = coord[0]
lon = coord[1]
urlTotal = urlBase + "lat="+ str(lat) + "&lon=" + str(lon) +"&appid=" + key
#actually call the api for data!
while(True):
    response = requests.get(urlTotal)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temp = main['temp']
        hum = main['humidity']
        pres = main['pressure']
        report = data['weather']
        descript = report[0]['description']
        words = descript.split()
        far = ((temp-273.15) * (1.8)) + 32
        #temp colors
        print("Colors Turning on:")
        if far > 32:
            GPIO.output(13, GPIO.HIGH)
            print("Red")
        if far > 50:
            GPIO.output(19, GPIO.HIGH)
            print("Yellow")
        if far > 65:
            GPIO.output(26, GPIO.HIGH)
            print("Green")
        for word in words:
            if word in rain:
                GPIO.output(17, GPIO.HIGH)
                print("Blue")
        print("Temp (F): " + str(far))
        print(words)
        print("===================================================")
        #wait before another check, reset lights for a moment!
        time.sleep(600)
        print("Reseting...")
        GPIO.output(13, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
    else:
        print("Error in HTTP request!")
        time.sleep(600)
