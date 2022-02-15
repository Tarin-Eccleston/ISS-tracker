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



# print(output)

# Extract TLE lines
# name = output.split('\n', 1)[1]
# line1 = output.split('\n', 2)[1]
# line2 = output.split('\n', 3)[1]

# print(name)

# ts = skyfield.api.load.timescale()
# satellite = EarthSatellite(line1, line2, name, ts)




