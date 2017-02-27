# Pi-Ping
A quick and simple Python script that checks the status of a website, then uses ThingM's blink(1) USB RGB LED notification light to provide a visual indication of the status.

## Installation
This requires a few pre-requistes:
* ThingM's blink(1)
* pip
* requests

### ThingM's blink(1)
Install in your command line with:

```sudo apt-get install libusb-1.0-0-dev
git clone https://github.com/todbot/blink1.git
cd blink1/commandline
make```

Update udev rules so you don't need to run as `sudo` every time:

```cd blink1/linux
sudo cp 51-blink1.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
```

Unplug the blink(1) and put it back in to complete the process.

### pip
Install Python 2 and 3 versions in your command line with:

```sudo apt-get install -y python-pip python3-pip```

### requests
Install in your command line with:

```sudo pip install requests