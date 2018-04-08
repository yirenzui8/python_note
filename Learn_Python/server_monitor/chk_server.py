#!/usr/bin/env python
import requests
r = requests.get('http://123.57.159.175/gnudip/cgi-bin/gnudip.cgi')
if r.status_code == requests.codes.ok:
    print (r.status_code)
