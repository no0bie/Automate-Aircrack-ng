echo "Available commands: "
echo "-h		Help Menu"
echo "-mc		Monitor a network"
echo "-m		See all the networks around you"
echo "-si		Start your interface on monitor mode"
echo "-i		Install all that is required"
echo "-d		Try and capture a handshake"
read option
python3 ./automation.py $option