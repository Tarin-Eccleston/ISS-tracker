import time
import math
import datetime
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

dt = 0.015

while True:
    t = ts.now()

    geocentric = satellite.at(t)
    # v = satellite.at(t).velocity()
    
    lat, lon = wgs84.latlon_of(geocentric)
    lat = lat.degrees
    lon = lon.degrees
    
    alt = wgs84.height_of(geocentric)
    alt = alt.km

    time.sleep(dt)


