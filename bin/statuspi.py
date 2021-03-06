# This file is part of statuspi.py, available at
# <github.com/h2g2guy/statuspi.py>.

# statuspi.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import RPi.GPIO as GPIO
import subprocess, time, sys

def usage():
    print "usage: sudo python statuspi.py <cfg_file>"
    print "      the first line of the configuration file will be executed"
    print "      as a python script every five seconds; on a return code of"
    print "      1, the LED will illuminate.  otherwise, the LED will turn off."
    GPIO.cleanup()
    sys.exit()

GPIO.setmode(GPIO.BCM)

if len(sys.argv) != 2:
    usage();

with open(sys.argv[1]) as f:
    line = f.readline()[:-1];
    line2 = f.readline()
    if line2 is not None:
        line2 = line2[:-1]

# connect LED on pin 18
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

while True:
    if subprocess.call(["python", line]) == 1:
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)

    if line2 is not "" and line2 is not None and line2 is not '':
        if subprocess.call(["python", line2]) == 1:
            GPIO.output(23, True)
        else:
            GPIO.output(23, False)

    time.sleep(5)

