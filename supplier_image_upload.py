#!/usr/bin/env python3
import requests, os, sys

url = 'http://localhost/upload/'
path = 'supplier-data/images/'

images = os.listdir(path)

for image in images:
    if image.endswith('.jpeg'):
        with open(path + image, 'rb') as opened:
            r = requests.post(url, files={'file':opened})
