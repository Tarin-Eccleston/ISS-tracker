import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# get latitude, longitude, altitude and velocity information from API
url = "http://api.open-notify.org/iss-now.json"
# url = "https://api.wheretheiss.at/v1/satellites/25544"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("Latitude: " + result["iss_position"]["latitude"] + " , Longitude: " + result["iss_position"]["longitude"]) # +
    # " , Altitude: " + result["altitude"] + " , Velocity: " + result["velocity"])


