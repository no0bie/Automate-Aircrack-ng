# Automate Aircrack-ng
A simple script that will do everything to get a WPA handshake, without you memorising the commands

You control what step goes next

# Run
To run simply type
> python3 automation.py [-option]

# Options
```
	-h		Help Menu
	-mc		Monitor a network
	-m		See all the networks around you
	-si		Start your interface on monitor mode
	-i		Install all that is required
	-d		Try and capture a handshake
```

# Errors
The program requires a NODELETE.txt file which contins your mon network interface

If you run into any errors run
> python automation.py -si and then follow the steps and the file will be created 

Any other errors should be about python version.

If you're getting errors run the script with python 2.x

or

replace all the raw_input in the script with input

# Disclaimer
As always I'm not responsible for your actions
