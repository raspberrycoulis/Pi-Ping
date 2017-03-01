# Pi-Ping
A quick and simple Python script that checks the status of a website, then uses [ThingM's blink(1)](https://blink1.thingm.com/ "ThingM's blink(1)") USB RGB LED notification light to provide a visual indication of the status.

For those who are probably asking, "What is the blink(1)?", then this should help:

![ThingM's blink(1)](https://blink1.thingm.com/wp-content/uploads/2014/09/blink1_mk2_lifestyle_07-270x250.jpg)

## Installation
This requires a few pre-requistes:
* ThingM's blink(1)
* pip
* requests

### ThingM's blink(1)
Install in your command line with:

    $ sudo apt-get install libusb-1.0-0-dev git-core
    $ git clone https://github.com/todbot/blink1.git
    $ cd blink1/commandline
    $ make

Update udev rules so you don't need to run as `sudo` every time:

    $ cd blink1/linux
    $ sudo cp 51-blink1.rules /etc/udev/rules.d/
    $ sudo udevadm control --reload-rules

Unplug the blink(1) and put it back in to complete the process.

### pip
Install Python 2 and 3 versions in your command line with:

    $ sudo apt-get install -y python-pip python3-pip

### requests
Install in your command line with:

    $ sudo pip install requests

## Clone this repo
To clone this repo, run the following command in your command line:

    $ git clone https://github.com/raspberrycoulis/Pi-Ping.git

### Usage
The script will, by default, check the HTTP status of Google. You can change this in the code easily, by changing the `website` variable, replacing "https://www.google.co.uk" with your website.

Before running the script, make sure it is executable by running (assuming you have cloned this in your home directory):

    $ chmod +x pi-ping.py

Test out the script by running:

    $ ./pi-ping.py

If all goes well, the blink(1) should flash green or red depending on whether the site is up or down.

## Running on boot
The script is set to check the status of your set website every 30 minutes (1800 seconds), but to run this on boot you can do so using `systemd`:

### 1. Create Unit file
This will tell the Pi to run your script on boot:

    sudo nano /lib/systemd/system/ping.service

Then add the following text to your file (you may need to adjust the path for your `pi-ping.py` script depending on where it is located (the part `/home/pi/Pi-Ping/pi-ping.py`):

    [Unit]
    Description=Pi-Ping service by Raspberry Coulis
    After=multi-user.target

    [Service]
    Type=idle
    ExecStart=/usr/bin/python /home/pi/Pi-Ping/pi-ping.py

    [Install]
    WantedBy=multi-user.target

Exit, `ctrl + x`, and save `y` to create the service unit file.

### 2. Set the relevant permissions
Make sure that the permissions are set correctly:

    sudo chmod 644 /lib/systemd/system/ping.service

### 3. Configure systemd
Make sure that systemd can use your newly created unit file:

    sudo systemctl daemon-reload
    sudo systemctl enable ping.service

Reboot the Pi to test via `sudo reboot`.

### 4. Check on the status of your service
Check that the service has started by running:

    sudo systemctl status ping.service

If done correctly, you should see that your `pi-ping.py` script is now running!

## Going further
It is very easy to change the colours or the number of times the LED blinks by editing the relevant parts in the `pi-ping.py` file. It should be pretty self-explanatory, but there is a lot more information on the [ThingM Github page regarding the command line tool](https://github.com/todbot/blink1/blob/master/docs/blink1-tool.md)!

Also, if you feel you can improve this script then please feel free to contribute!