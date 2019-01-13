# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:55:12 2019

@author: Bob
"""

import numpy as np

def Haversine(location_1, location_2, unit='miles'):
    
    conversion = {'miles': 1609.344,
                  'kilometers': 1000.000,
                  'feet': 0.3047851,
                  'meters': 1}
    lat1, long1 = location_1[0], location_1[1]
    lat2, long2 = location_2[0], location_2[1]
    
    RADIUS = 6371000 # Radius of the earth in meters
    
    lat1 = np.deg2rad(lat1)
    long1 = np.deg2rad(long1)
    lat2 = np.deg2rad(lat2)
    long2 = np.deg2rad(long2)
    
    delta_lat = lat2 - lat1
    delta_long = long2 - long1
    
    a = (np.sin(delta_lat / 2.0) ** 2)
    a += np.cos(lat1) * np.cos(lat2) * np.sin(delta_long / 2.0) ** 2
    
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    d = RADIUS * c
    return d / conversion[unit]
