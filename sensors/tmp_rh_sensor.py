#!/usr/bin/python
import Adafruit_DHT as dht

def read_tmp_rh():
    h, t = dht.read_retry(dht.DHT22, 4)
    return {'tmp': t, 'rh': h}
