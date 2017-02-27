#!/usr/bin/python

import requests
import os

website = "https://ghostpi.pro/"

response = requests.get(website)

if int(response.status_code) == 200: # OK
    os.system("./blink1/commandline/blink1-tool -q -m 500 --green --blink 3")
    
elif int(response.status_code) == 500: # Internal server error
    os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")

elif int(response.status_code) == 503: # Service unavailable
    os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")

elif int(response.status_code) == 502: # Bad gateway
    os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")

elif int(response.status_code) == 520: # Cloudflare: Unknown error
    os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")
    
elif int(response.status_code) == 522: # Cloudflare: Connection timed out
    os.system("./blink1/commandline/blink1-tool -q -m 300 --red --blink 5")
    
elif int(response.status_code) == 523: # Cloudflare: Origin is unreachable
    os.system("./blink1/commandline/blink1-tool -q -m 300 --red --blink 10")
    
elif int(response.status_code) == 524: # Cloudflare: A Timeout occurred
    os.system("./blink1/commandline/blink1-tool -q -m 500 --red --blink 3")