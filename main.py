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

dt = 0.02
# R = 6371
# lat_prev = 0.0
# lon_prev = 0.0
# count = 0

while True:
    t = ts.now()

    geocentric = satellite.at(t)
    # v = satellite.at(t).velocity()
    
    lat_current, lon_current = wgs84.latlon_of(geocentric)
    lat_current = lat_current.radians
    lon_current = lon_current.radians
    
    alt = wgs84.height_of(geocentric)
    alt = alt.km
    
    # if (~(lat_prev == 0.0) & ~(lon_prev == 0.0) & (count % 1000 == 0)):
    #     # use Haversine formala to find ISS velocity
    #     dlong = lon_current - lon_prev;
    #     dlat = lat_current - lat_prev;
        
    #     dtheta = 2 * math.asin(math.sqrt(pow(math.sin(dlat / 2), 2) + math.cos(lat_prev) * 
    #         math.cos(lat_current) * pow(math.sin(dlong / 2), 2)))
    #     ds = R * dtheta
        
    #     # differentiate to find velocity
    #     v = ds/(dt * 1000)
    #     v = round(v,4)
    #     print("Velocity (km/s): " + str(v))


    # if (count % 1000 == 0): 
    #     lat_prev = lat_current
    #     lon_prev = lon_current
    
    # count = count + 1
    time.sleep(dt)


