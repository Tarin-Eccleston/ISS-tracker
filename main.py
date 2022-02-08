import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder
import math

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

# initialise for Havresine formula
lat_prev = 0.0
lon_prev = 0.0
# radius of earth
R = 6371

while True:

    # get latitude, longitude from API
    url = "http://api.open-notify.org/iss-now.json"
    start = time.time()
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # find and save lat and lon
    lat_current = result["iss_position"]["latitude"]
    lon_current = result["iss_position"]["longitude"]
    print("Latitude: " + lat_current + " , Longitude: " + lon_current)
    lat_current = float(lat_current)
    lon_current = float(lon_current)

    time.sleep(1)
    end = time.time()

    iss.goto(lon_current, lat_current)

    dt = end - start
    print(dt)

    # use Havresine formala to find ISS velocity
    dlong = lon_current - lon_prev;
    dlat = lat_current - lat_prev;
    
    dtheta = 2 * math.asin(math.sqrt(pow(math.sin(dlat / 2), 2) + math.cos(lat_prev) * 
        math.cos(lat_current) * pow(math.sin(dlong / 2), 2)))

    ds = R * dtheta
        
    v = ds/dt
    print(v)

    lat_prev = lat_current
    lon_prev = lon_current

