"""Functions related to locations."""

from math import asin, cos, radians, sin, sqrt


def distance_covered(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points on the earth.
    (specified in decimal degrees) and returns the distance in meters.
    lon1 - longitude1 lon2 - longitude2
    lat1 - lattitude1 lat2 - lattitude2
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    meters = 6367 * c * 1000
    return meters
