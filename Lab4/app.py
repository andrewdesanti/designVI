import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import socket
import smtplib

senderAddress = "xxxx@gmail.com"
recieverAddress = "xxxx@xxx.xxx"
senderPassword = "xxxxxxxx"
subject = "Hey Andy, Someone Clicked the Button!"
body = "Ask around the house!"

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

pins = {
   23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
   24 : {'name' : 'GPIO 24', 'state' : GPIO.LOW}
   }

@app.route("/email")
def sendMail():
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp_server.login(senderAddress, senderPassword)
    message = f"Subject: {subject}\n\n{body}"
    smtp_server.sendmail(senderAddress, recieverAddress, message)
    templateData = {
      'pins' : pins }
    return render_template('main.html', **templateData)

for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   templateData = {
      'pins' : pins
      }
   return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
   
   changePin = int(changePin)
   
   deviceName = pins[changePin]['name']
   
   if action == "on":
      GPIO.output(changePin, GPIO.HIGH)
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
