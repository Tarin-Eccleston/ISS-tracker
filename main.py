import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# get latitude, longitude from API
url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("Latitude: " + result["iss_position"]["latitude"] + " , Longitude: " + result["iss_position"]["longitude"])

webbrowser.open("iss.txt")

# setup screen for world map
screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,180,90)

# load image of world map
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup

input("out")
