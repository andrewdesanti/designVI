# CPE-322: Engineering Design VI: Stevens Spring 2021
## Lab2
This folder contains a very simple python script "simpleLight.py", that interacts with the simple LED circuit from Lab2, causing an LED to blink. 

While there are a few Python libraries that interact with Raspberry Pi GPIO ports, this program in particular utilizes gpiozero. 

If you plan on running this yourself, be careful which pins are defined in the code AND where you are jumping your wires from!

## Lab4
This folder contains a very simple Flask Server that can be used to interact with LEDs connected to Raspberry Pi GPIO ports. 

The hosted site has three buttons, two that toggle LEDs, and one that sends an automated email via a Gmail account to my personal email letting me know someone pinged it. 

This particlar program uses RPi.GPIO instead of gpiozero to interact with GPIO pins. 

Again be careful about what pins you are using!

## Weather
This is a simple Python program that makes use of OpenWeatherMap and GeoCoder to estimate the coordinates of your machine and display the weather conditions via a few LEDs wired up to Raspberry Pi GPIO pins. 

Before you can use it, you will need to first ensure the pins you are using are correct! Using the wrong pins or editing the file incorrectly may damage your device!

You must also get your own API key for OpenWeatherMap for free. This requires making an account which is free albiet with fewer features!

## website
At the moment this is nothing more than a Django server that hosts a dummy blog. I took the time to add some fancier HTML, CSS, and JS, but it does not at the moment have an actual function.

It isn't much now but I do plan on diving deeper into this over the summer as I have been particularly inspired to delve deeper into web-dev and IoT from this class.
