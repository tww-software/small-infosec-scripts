#!/bin/bash
if [ $UID != 0 ];
then
echo "must be root to run this"
exit 1
fi
echo "enter interface :"
read interface
echo " enter new MAC address format XX:XX:XX:XX:XX:XX :"
read newmac
ifconfig $interface down
ifconfig $interface hw ether $newmac
ifconfig $interface up
if [ $? == 0 ];
then
echo "MAC address of $interface changed to $newmac"
else
echo "MAC address change failed"
exit 1
fi

