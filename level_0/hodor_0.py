#!/usr/bin/python3
import requests


payload = {'id': 766, 'holdthedoor': 'Submit'}
for i in range(1024):
    r = requests.post("http://158.69.76.135/level0.php", data=payload)