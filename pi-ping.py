#!/usr/bin/python

# This Python script will ping a website and return the relevant HTTP status code.
# It will then issue a command using the blink1-tool to blink a RGB LED, providing
# a visual indication of the website's status:
#
# Green = website is up and running
# Red = website is not working properly
#
# More on HTTP status codes found here: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#
# Feel free to improve as I made this quickly and I'm not a coding ninja!
#
# By: Wesley Archer (aka. Raspberry Coulis)
# Web: https://www.raspberrycoulis.co.uk
# Twitter: https://twitter.com/raspberrycoulis
# Email: wesley@raspberrycoulis.co.uk
#

import requests
import os
import time

website = "https://ghostpi.pro/"    # Replace this with the website you want to ping
wait = 1800   # Time (in seconds) in between pings - Default: 1800 (30 mins)

def ping():
  while True:
    response = requests.get(website)

    if int(response.status_code) == 200: # OK
      os.chdir("/home/pi/")
      os.system("./blink1/commandline/blink1-tool -q -m 500 --green --blink 3")

    elif int(response.status_code) == 500: # Internal server error
      os.chdir("/home/pi/")
      os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")
    
    elif int(response.status_code) == 503: # Service unavailable
      os.chdir("/home/pi/")
      os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")
    
    elif int(response.status_code) == 502: # Bad gateway
      os.chdir("/home/pi/")
      os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")
    
    elif int(response.status_code) == 520: # Cloudflare: Unknown error
      os.chdir("/home/pi/")
      os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")
    
    elif int(response.status_code) == 522: # Cloudflare: Connection timed out
      os.chdir("/home/pi/")      
      os.system("./blink1/commandline/blink1-tool -q -m 300 --red --blink 5")
    
    elif int(response.status_code) == 523: # Cloudflare: Origin is unreachable
      os.chdir("/home/pi/")
      os.system("./blink1/commandline/blink1-tool -q -m 300 --red --blink 10")
    
    elif int(response.status_code) == 524: # Cloudflare: A Timeout occurred
      os.chdir("/home/pi/")
      os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")

    time.sleep(wait)

ping()