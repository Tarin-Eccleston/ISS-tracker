import time
import math
import datetime
from black import out
import requests
import skyfield
from skyfield.api import EarthSatellite

# Make reques to ISS API for TLE data lines
f = requests.get('https://api.wheretheiss.at/v1/satellites/25544/tles?format=text')
output = f.text
output = output.split('\n', 3)

# Extract TLE lines
name = output[0]
line1 = output[1]
line2 = output[2]

# ts = skyfield.api.load.timescale()
# satellite = EarthSatellite(line1, line2, name, ts)




