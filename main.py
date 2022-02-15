import time
import math
import datetime
from black import out
import requests
import skyfield
from skyfield.api import EarthSatellite, wgs84

# Make request to ISS API for TLE data lines
f = requests.get('https://api.wheretheiss.at/v1/satellites/25544/tles?format=text')
output = f.text
output = output.split('\n', 3)

# Extract TLE lines
name = output[0]
line1 = output[1]
line2 = output[2]

ts = skyfield.api.load.timescale()
satellite = EarthSatellite(line1, line2, name, ts)

print(satellite)

# Can't seem to find the UTC time now
# t = ts.now()

# days = t - satellite.epoch
# print('{:.3f} days away from epoch'.format(days))

# if abs(days) > 7:
#     print("TLE epoch is too far in the past/future")

while True:
    t = ts.now()

    geocentric = satellite.at(t)
    lat, lon = wgs84.latlon_of(geocentric)
    print(lat)
    print(lon)

    time.sleep(0.02)


