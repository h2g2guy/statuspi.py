statuspi.py
===========

A simple headless status box utility for the Raspberry Pi.  Released
under the GPL.

Setup
-----

Download the script, then install the GPIO library:

    sudo pip install rpi.gpio

Then write your own python script to define when you want your LED to
illuminate.  This script will be called with a five second delay each time.
When your script returns 1, the LED will illuminate; when the script
returns anything else, the light will turn off.

Finally, wire up the LED to pin 18 and ground.  For you non-hardware types,
here's a quick explanation:  connect the longer lead of the LED to GND,
and the shorter lead to an empty space on your breadboard.  Connect that
shorter lead to a 220 Ohm or greater resistor, and connect the other end of
the resistor to the pin on your breakout board that reads '#18'.

Usage
-----

This script **must** be run as su, or the GPIO library won't be able to
access the hardware correctly.  Usage is as follows:

    sudo python statuspi.py <your script>

To do
-----

- Gracefully closing the GPIO library
- Allowing the use of multiple scripts and multiple LEDs through a yaml
    config file
- Customizable repeat time for scripts

License
-------

statuspi.py is licensed under the GPLv3.  See `LICENSE` for details.
