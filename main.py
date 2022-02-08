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
initial = True
R = 6371
dt = 5

while True:
    # get latitude, longitude from API
    url = "http://api.open-notify.org/iss-now.json"
    start = time.time()
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # extract from data
    timestamp = result["timestamp"]
    lat_current = result["iss_position"]["latitude"]
    lon_current = result["iss_position"]["longitude"]
    print("Timestamp: " + str(timestamp))
    print("Latitude: " + lat_current + " , Longitude: " + lon_current)

    # update iss map with new coordinates
    lat_current = float(lat_current)
    lon_current = float(lon_current)
    iss.goto(lon_current, lat_current)

    #  convert coordinates to radians
    lon_current = lon_current * math.pi/180
    lat_current = lat_current * math.pi/180

    # calculate server request delay to accept/reject measurements
    end = time.time()
    delay = end - start

    if (~(lat_prev == 0.0) & ~(lon_prev == 0.0) & ((delay <= 1.0) | (delay >= 0.1))):
        # use Haversine formala to find ISS velocity
        dlong = lon_current - lon_prev;
        dlat = lat_current - lat_prev;
        
        dtheta = 2 * math.asin(math.sqrt(pow(math.sin(dlat / 2), 2) + math.cos(lat_prev) * 
            math.cos(lat_current) * pow(math.sin(dlong / 2), 2)))
        ds = R * dtheta
        
        # differentiate to find velocity
        v = ds/dt
        v = round(v,4)
        print("Velocity (km/s): " + str(v))

    lat_prev = lat_current
    lon_prev = lon_current
    time.sleep(dt)


