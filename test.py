#!/usr/bin/python3
import requests


r = requests.post("http://158.69.76.135/level0.php")

print(r.text)