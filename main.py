import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# setup screen for map
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:

    # get latitude, longitude from API
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    lat = result["iss_position"]["latitude"]
    lon = result["iss_position"]["longitude"]

    print("Latitude: " + lat + " , Longitude: " + lon)

    lat = float(lat)
    lon = float(lon)

    iss.goto(lon, lat)

    time.sleep(1)

